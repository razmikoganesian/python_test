import asyncio


async def brew_tea():
    print("Brewing tea...")
    await asyncio.sleep(2)
    print("Tea is Ready!")


asyncio.run(brew_tea())
