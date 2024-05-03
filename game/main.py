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
    row, column = (5, 5,)

    coroutine = blink(canvas, row, column)
    # while True:
    #     try:
    #         coroutine.send(None)
    #         canvas.refresh()
    #         time.sleep(0.5)
    #     except StopIteration:
    #         break

    # canvas.addstr(row, column, "*", curses.A_DIM)
    coroutine.send(None)
    canvas.refresh()
    time.sleep(2)

    # canvas.addstr(row, column, "*")
    coroutine.send(None)
    canvas.refresh()
    time.sleep(.3)

    # canvas.addstr(row, column, "*", curses.A_BOLD)
    coroutine.send(None)
    canvas.refresh()
    time.sleep(.5)

    # canvas.addstr(row, column, "*")
    coroutine.send(None)
    canvas.refresh()
    time.sleep(.3)

    canvas.clear()
    canvas.border()
    canvas.refresh()
    time.sleep(30)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
