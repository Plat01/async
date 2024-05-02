import asyncio
import curses

import random
import time


async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        await asyncio.sleep(2)

        canvas.addstr(row, column, symbol)
        for i in range(3):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        for i in range(5):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for i in range(3):
            await asyncio.sleep(0)


def draw(canvas):
    tic_timeout = 0.1
    shapes = '+*.:'
    curses.curs_set(False)
    canvas.border()
    rows, columns = canvas.getmaxyx()
    coroutines = []
    for i in range(100):
        coroutine = asyncio.create_task(blink(canvas=canvas,
                                              row=random.randrange(1, rows - 1),
                                              column=random.randrange(1, columns - 1),
                                              symbol=random.choice(shapes)))
        coroutines.append(coroutine)
    while True:
        for coroutine in coroutines:
            coroutine.send(None)
            canvas.refresh()
        time.sleep(tic_timeout)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)



