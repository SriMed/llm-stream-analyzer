from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Event(BaseModel):
    timestamp: str
    service: str
    level: str
    message: str
    metadata: dict | None = None

class AnalysisResult(BaseModel):
    severity: str
    summary: str
    is_anomaly: bool
    anomaly_reason: str | None = None
    tags: list[str] = []

@router.post("/analyze", response_model=AnalysisResult)
def analyze_event(event: Event):
    # placeholder before LLM
    return AnalysisResult(
        severity="medium",
        summary=f"Stub summary for: {event.message}",
        is_anomaly=False,
        anomaly_reason=None,
        tags=[event.service, event.level.lower()],
    )
