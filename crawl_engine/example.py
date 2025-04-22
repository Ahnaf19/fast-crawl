import asyncio
from crawl4ai import AsyncWebCrawler

async def main(target_url: str):
    """quick example of how to use the AsyncWebCrawler class"""
    async with AsyncWebCrawler() as crawler:
        # Start crawling from the given URL
        result = await crawler.arun(url=target_url)

        # extracted content as md
        print(result.markdown) # type: ignore

if __name__ == "__main__":
    target_url = "https://www.techwithtim.net/"
    asyncio.run(main(target_url))