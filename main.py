import asyncio
import aiohttp

API_KEY = '67ba5fb26dc84fa880b112116250903'  
CITIES = ['London', 'Paris', 'Berlin', 'Madrid', 'Rome','Thailand']

async def fetch_weather(session, city):
    url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}'
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_weather(session, city) for city in CITIES]
        results = await asyncio.gather(*tasks)
        for city, data in zip(CITIES, results):
            print(f"Weather in {city}: {data['current']['condition']['text']}")

if __name__ == '__main__':
    asyncio.run(main())