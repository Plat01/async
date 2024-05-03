import asyncio
import curses
import random
import time


async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        for _ in range(10):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(3):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        for _ in range(5):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(3):
            await asyncio.sleep(0)


def draw(canvas: curses.window):
    curses.curs_set(False)
    canvas.border()
    size = canvas.getmaxyx()
    symbols = '+*.:'
    # canvas.addstr(random.randint(1, size[0]), random.randint(1, size[1]), str(size))
    # canvas.refresh()
    # time.sleep(10)

    coroutines = [blink(canvas,
                        random.randint(1, size[0] - 2),
                        random.randint(1, size[1] - 2),
                        symbol=random.choice(symbols)) for _ in range(500)]

    # coroutines = [blink(canvas, 5, (i + 1) * 5) for i in range(10)]
    #
    while True:
        for coroutine in coroutines:
            coroutine.send(None)
        canvas.refresh()
        time.sleep(0.1)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
