from fastapi.routing import APIRouter
from ..core.models import GitHubPayload, TelexWebhookPayload
from ..config.config import settings
from ..utils.telex_utils import send_payload
from fastapi.responses import JSONResponse
from fastapi import status, HTTPException
import json


router = APIRouter(prefix="/github")


@router.post("/{telex_channel_id}", status_code=status.HTTP_200_OK)
async def github_webhook(telex_channel_id: str, payload: GitHubPayload):
    """Endpoint to receive GitHub webhook events and forward the commits to Telex."""
    telex_payload = TelexWebhookPayload(
        event_name="pushed_commits",
        message=str(payload.commits),
        status="success",
        username=payload.pusher["name"],
    ).model_dump_json()

    telex_url = f"{settings.telex_webhook_url}/{telex_channel_id}"

    try:   
        response = await send_payload(telex_payload, telex_url)
        response_data = json.loads(response.decode().strip())
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Telex payload sending failed: {str(e)}",
        )

    return JSONResponse(content={"data": response_data})
