import asyncio
import curses
import time


async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)


def draw(canvas: curses.window):
    curses.curs_set(False)
    canvas.border()

    coroutines = [blink(canvas, 5, (i + 1) * 5) for i in range(5)]

    while True:
        for coroutine in coroutines:
            coroutine.send(None)
        canvas.refresh()
        time.sleep(0.5)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
