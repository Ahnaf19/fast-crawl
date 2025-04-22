from fastapi import APIRouter
from pydantic import HttpUrl

from app.models.crawl_models import CrawlResponse
from crawl_engine.crawl_engine import crawl_batch

router = APIRouter(prefix="/crawl", tags=["crawl"])

@router.post("/single", response_model=CrawlResponse)
async def crawl_url(url: HttpUrl):
    await crawl_batch([str(url)])

@router.post("/batch", response_model=CrawlResponse)
async def crawl_urls(urls: list[str]):
    await crawl_batch(urls)