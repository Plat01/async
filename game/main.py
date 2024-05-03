import asyncio
import curses
import random
import time


async def blink(canvas, row, column, symbol='*', max_delay=4):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        for _ in range(random.randint(1, max_delay)):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(random.randint(1, max_delay)):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        for _ in range(random.randint(1, max_delay)):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(random.randint(1, max_delay)):
            await asyncio.sleep(0)


def draw(canvas: curses.window):
    curses.curs_set(False)
    canvas.border()
    size = canvas.getmaxyx()
    symbols = '+*.:'

    coroutines = [blink(canvas,
                        random.randint(1, size[0] - 2),
                        random.randint(1, size[1] - 2),
                        symbol=random.choice(symbols)) for _ in range(500)]

    while True:
        for coroutine in coroutines:
            coroutine.send(None)
        canvas.refresh()
        time.sleep(0.1)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
