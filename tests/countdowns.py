import asyncio


async def countdown(frm: int = 0, to: int = 10):
    for i in range(frm, to):
        print(i)
        await asyncio.sleep(1.)


async def main():
    # await countdown()
    # await countdown(100, 110)
    await asyncio.gather(countdown(), countdown(100, 110))


if __name__ == '__main__':
    asyncio.run(main())
