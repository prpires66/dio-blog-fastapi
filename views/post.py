from datetime import datetime, timezone
from pydantic import BaseModel, AwareDatetime, field_validator


class PostOut(BaseModel):
    id: int
    title: str
    content: str
    published_at: AwareDatetime | None = None

    @field_validator("published_at", mode="before")
    @classmethod
    def ensure_timezone(cls, v: datetime | None) -> datetime | None:
        if v is not None and v.tzinfo is None:
            return v.replace(tzinfo=timezone.utc)
        return v