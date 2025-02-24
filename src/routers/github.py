from fastapi.routing import APIRouter
from ..core.models import GitHubPayload, TelexWebhookPayload
from typing import Annotated
from ..core.analyzer.analyzer import CommitAnalyzer
from ..config.config import settings
from ..utils.telex_utils import send_payload
from fastapi.responses import JSONResponse
from fastapi import status, HTTPException, Query
import json


router = APIRouter(prefix="/github")


@router.post("/{telex_channel_id}/", status_code=status.HTTP_200_OK)
async def github_webhook(
    telex_channel_id: str,
    payload: GitHubPayload,
    is_test: Annotated[str | None, Query()] = None,
):
    """
    Endpoint to receive GitHub webhook events, analyze commit messages and
    send results to Telex if issues are found.
    """
    analyzer = CommitAnalyzer()
    commits = payload.commits
    all_messages = []  # Accumulate messages for test mode

    for commit in commits:
        violations = analyzer.analyze_commit(commit["message"])
        if violations:
            output_message = analyzer.format_analysis(commit, violations)
            if is_test.lower() == "true":
                all_messages.append(output_message)
            else:
                telex_payload = TelexWebhookPayload(
                    event_name="pushed_commits",
                    message=output_message,
                    status="success",
                    username=payload.pusher["name"],
                ).model_dump_json()

                telex_url = f"{settings.telex_webhook_url}/{telex_channel_id}"

                try:
                    await send_payload(telex_payload, telex_url)
                except Exception as e:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Telex payload sending failed: {str(e)}",
                    )
    if is_test.lower() == "true":
        return JSONResponse(content=all_messages, status_code=status.HTTP_200_OK)

    return JSONResponse(content={"status": "success"})
