from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, MemoryAdaptiveDispatcher
import asyncio
from loguru import logger

from app.models.crawl_models import CrawlResponse


async def crawl_batch(urls: list[str]):
    """
    Crawl a batch of URLs asynchronously and process the results.
    Args:
        urls (list[str]): A list of URLs to crawl.
    Returns:
        list: A list of processed responses for successfully crawled URLs.
    Raises:
        HTTPException: If crawling the first URL in the batch fails.
    """
    
    browser_config = BrowserConfig(headless=True, verbose=False)
    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        check_robots_txt=True,
        stream=False # default: getting all results at once
    )
    
    dispatcher = MemoryAdaptiveDispatcher(
        memory_threshold_percent=70.0,
        check_interval=1.0,
        max_session_permit=10
    )
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        results = await crawler.arun_many(
            urls=urls,
            run_config=run_config,
            dispatcher=dispatcher
        )
        
        responses = []
        for result in results: # type: ignore
            if result.success:
                response = await process_result(result)
                responses.append(response)
            else:
                logger.error(f"Failed to crawl {result.url}: {result.error_message}")        
    
    return responses

async def process_result(result):
    """Process a successful crawl result and return a structured data.

    Args:
        result (CrawlResult): CrawlResult object containing page data and metadata
    """
    
    logger.info(f"\n\nprocessing: {result.url}")
    logger.info(f"status_code: {result.status_code}")
    
    content_preview = None
    if result.markdown:
        # remove extra spaces and newlines from the markdown text
        # and limit the preview to 150 characters
        clean_text = ' '.join(result.markdown.split())
        content_preview = clean_text[:150] + '...' if len(clean_text) > 150 else clean_text
        
        logger.info(f"content preview: {content_preview}")
    
    # process metadata
    if result.metadata:
        logger.info(f"\n\nmetadata:")
        for key, val in result.metadata.items():
            logger.info(f"{key}: {val}")
            
    # process links found on the page
    if result.links:
        internal_links = result.links.get('internal', [])
        external_links = result.links.get('external', [])
        logger.info(f"Found {len(internal_links)} internal links.")
        logger.info(f"Found {len(external_links)} internal links.")
    
    logger.info("-" * 80)
    
    return CrawlResponse(
        url=result.url,
        status_code=result.status_code,
        content_preview=content_preview,
        metadata=result.metadata,
        internal_link_count=len(internal_links),
        external_link_count=len(external_links)
    )  

if __name__ == "__main__":  
    urls = [
        "https://www.techwithtim.net/",
        "https://www.techwithtim.net/tutorials",
        "https://www.techwithtim.net/courses",
        "https://www.techwithtim.net/newsletter",
        "https://www.youtube.com/watch?v=K9anz4aB0S0"
    ]
    
    responses = asyncio.run(crawl_batch(urls))
    logger.info(f"responses len: {len(responses)}")
    logger.info(responses)