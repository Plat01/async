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

    i = 0
    coroutine = blink(canvas, row, column)
    while True:
        try:
            coroutine.send(None)
            # print(i := i + 1)
            # canvas.addstr(row, column, str(i), curses.A_BOLD)
            canvas.refresh()
            time.sleep(0.5)
        except StopIteration:
            break


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
