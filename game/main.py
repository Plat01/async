import asyncio
import curses
import random
import time

from animation import animate_spaceship
from curses_tools import read_controls


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
    row_max_canvas, column_max_canvas = size[0] - 2, size[1] - 2
    symbols = '+*.:'

    coroutines = [blink(canvas,
                        random.randint(1, row_max_canvas),
                        random.randint(1, column_max_canvas),
                        symbol=random.choice(symbols)) for _ in range(100)]

    # coroutines.append(fire(canvas,
    #                        row_max_canvas,
    #                        10,
    #                        ))

    coroutines.append(animate_spaceship(canvas,
                                        random.randint(1, row_max_canvas),
                                        random.randint(1, column_max_canvas),
                                        row_max_canvas,
                                        column_max_canvas,
                                        2,
                                        1))

    while True:
        try:
            for coroutine in coroutines:
                coroutine.send(None)
            canvas.refresh()
            time.sleep(0.1)
        except StopIteration:
            break

    time.sleep(1)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
