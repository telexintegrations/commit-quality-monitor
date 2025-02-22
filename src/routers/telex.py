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
    """
    Handle incoming webhook from Telex. Analyzes commit messages and sends
    results to Slack if issues are found.
    """
    try:
        commit_message = ast.literal_eval(payload.message.replace("\n", "\\n"))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error evaluating telex payload string: {str(e)}",
        )
    try:
        analyzer = CommitAnalyzer(settings=payload.settings)
        slack_url = analyzer.slack_url
        
        all_messages = []  # Accumulate messages for test mode
        
        for commit in commit_message:
            violations = analyzer.analyze_commit(commit["message"])
            if violations:
                output_message = {"text": analyzer.format_analysis(commit, violations)}
                if is_test == "true":
                    all_messages.append(output_message["text"])
                else:
                    try:   
                        await send_payload(json.dumps(output_message), slack_url)
                    except Exception as e:
                        raise HTTPException(
                            status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Telex payload sending failed: {str(e)}",
                        )

        if is_test == "true":
            return JSONResponse(
                content=all_messages,
                status_code=status.HTTP_200_OK,
            )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error analyzing commits: {str(e)}",
        )

    return JSONResponse(content={"status": "success"}, status_code=status.HTTP_200_OK)


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