from pydantic import BaseModel

class CrawlResponse(BaseModel):
    url: str
    status_code: int
    content_preview: str | None = None
    metadata: dict | None = None
    internal_link_count: int | None = None
    external_link_count: int | None = None