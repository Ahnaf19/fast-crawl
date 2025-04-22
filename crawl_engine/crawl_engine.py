from multiprocessing import process
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, CrawlerMonitor, DisplayMode, MemoryAdaptiveDispatcher
import asyncio
from loguru import logger

async def crawl_batch():
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
    
    urls = [
        "https://www.techwithtim.net/",
        "https://www.techwithtim.net/tutorials",
        "https://www.techwithtim.net/courses",
        "https://www.techwithtim.net/newsletter"
    ]
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        results = await crawler.arun_many(
            urls=urls,
            run_config=run_config,
            dispatcher=dispatcher
        )
        
        for result in results: # type: ignore
            if result.success:
                await process_result(result)
            else:
                logger.error(f"Failed to crawl {result.url}: {result.error_message}")

async def process_result(result):
    """Process a successful crawl result.

    Args:
        result (CrawlResult): CrawlResult object containing page data and metadata
    """
    
    logger.info(f"\n\nprocessing: {result.url}")
    logger.info(f"status_code: {result.status_code}")
    
    if result.markdown:
        # remove extra spaces and newlines from the markdown text
        # and limit the preview to 150 characters
        clean_text = ' '.join(result.markdown.split())
        preview = clean_text[:150] + '...' if len(clean_text) > 150 else clean_text
        
        logger.info(f"content preview: {preview}")
    
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
    

if __name__ == "__main__":
    asyncio.run(crawl_batch())