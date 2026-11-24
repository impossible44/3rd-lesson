import asyncio
import aiohttp
import time

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()
async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks= [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results
urls= [
    'python.org',
    'yandex.ru',
    'lenta.ru'
]

start=time.time()
results=asyncio.run(fetch_all(urls))
end=time.time()
print(f"Загрузка {len(urls)} заняла {end - start:.2f} секунд")