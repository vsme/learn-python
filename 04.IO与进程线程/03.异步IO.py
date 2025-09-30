# 异步网络示例：并发抓取多个网页的前 N 字节
import asyncio

import aiohttp


async def head(url):
    async with aiohttp.ClientSession() as s:
        async with s.get(url) as r:
            return await r.text()


async def main():
    urls = ["https://example.com", "https://httpbin.org/get"]
    texts = await asyncio.gather(*(head(u) for u in urls))
    for t in texts:
        print(len(t))


asyncio.run(main())
