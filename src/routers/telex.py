from fastapi.routing import APIRouter
from ..core.models import TelexTargetPayload
from ..core.analyzer.analyzer import CommitAnalyzer
from ..config.integration_config import generate_json_config
from fastapi.responses import JSONResponse
from fastapi import status, HTTPException, Query
from typing import Annotated
import ast
from ..utils.telex_utils import send_payload
import json


router = APIRouter(prefix="/telex")
telex_json_router = APIRouter()


@router.post("/", status_code=status.HTTP_200_OK)
async def telex_webhook(
    payload: TelexTargetPayload, is_test: Annotated[str | None, Query()] = None
):
    """Handle incoming webhook from Telex and send results to Slack if webhook is provided."""
    commit_message = payload.message

    try:
        for setting in payload.settings:
            slack_url = setting["default"] if setting["label"] == "slack_url" else None

        if is_test.lower() == "true":
            return JSONResponse(content=commit_message, status_code=status.HTTP_200_OK)
        else:
            await send_payload(commit_message, slack_url)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Slack payload sending failed: {str(e)}",
        )


@telex_json_router.get("/integration.json", status_code=status.HTTP_200_OK)
async def get_integration_config() -> dict:
    """Endpoint to retrieve integration settings for Telex."""
    try:
        json_data = generate_json_config()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error retrieving config data: {str(e)}",
        )

    return json_data
