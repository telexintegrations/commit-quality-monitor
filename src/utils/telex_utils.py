import asyncio
from ..config.config import settings
from fastapi import HTTPException, status


async def send_payload(payload: str, url: str):
    """Sends payload through an asynchronous curl subprocess."""
    curl_command = [
        settings.curl_command,
        "-X",
        "POST",
        url,
        "-H",
        "Accept: application/json",
        "-H",
        "Content-Type: application/json",
        "-d",
        payload,
    ]
    process = await asyncio.create_subprocess_exec(
        *curl_command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()

    # Check for exit on error
    if process.returncode != 0:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Subprocess exception: {stderr.decode().strip()}",
        )

    return stdout
