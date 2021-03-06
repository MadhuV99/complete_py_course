import aiohttp
import asyncio
import async_timeout
import time


async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(f'Page took {time.time() - page_start} seconds')
            # print(response.status)
            # print(response.text())
            return await response.text()


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks

loop = asyncio.get_event_loop()
urls = ['https://google.com' for i in range(50)]
start = time.time()
pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
print(pages[0])
print(f'All pages took {time.time() - start} seconds')
