from fastapi.routing import APIRouter
from ..core.models import TelexTargetPayload
from ..core.analyzer import CommitAnalyzer
from ..config.integration_config import generate_json_config
from ..config.config import settings
from fastapi.responses import JSONResponse
from fastapi import status, HTTPException, Query
from typing import Annotated
import ast
import httpx


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
        commit_message = ast.literal_eval(payload.message)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error evaluating telex payload string: {str(e)}",
        )
    try:
        analyzer = CommitAnalyzer(settings=payload.settings)
        for commit in commit_message:
            violations = analyzer.analyze_commit(commit["message"])
            if violations:
                output_message = {"text": analyzer.format_analysis(commit, violations)}

                if is_test == "true":
                    return JSONResponse(
                        content=output_message["text"],
                        status_code=status.HTTP_200_OK,
                    )
                async with httpx.AsyncClient() as client:
                    await client.post(settings.slack_url, json=output_message)
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
