import aiohttp
import asyncio

async def open_website(user_id):
    url = "https://kcpt72.ru"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                print(f"User {user_id} opened the website. Status code: {response.status}")
    except Exception as e:
        print(f"User {user_id} failed to open the website. Error: {e}")

async def main():
    tasks = [open_website(i) for i in range(1000000)]
    await asyncio.gather(*tasks)

asyncio.run(main())