import asyncio
import time


async def brew(name):
    print(f"Brewing {name}...")
    # await asyncio.sleep(5)
    time.sleep(4)
    print(f" {name} is ready")


async def main():
    await asyncio.gather(brew("Masala tea"), brew("Ginger tea"), brew("Green tea"))


asyncio.run(main())
