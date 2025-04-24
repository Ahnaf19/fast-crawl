from fastapi import APIRouter

from app.models.crawl_models import CrawlResponse
from crawl_engine.crawl_engine import crawl_batch

router = APIRouter(prefix="/crawl", tags=["crawl"])

@router.post("/single")
async def crawl_url(url: str):
    return await crawl_batch([url])

@router.post("/batch")
async def crawl_urls(urls: list[str]):
    return await crawl_batch(urls)
