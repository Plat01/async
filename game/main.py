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


async def fire(canvas, start_row, start_column, rows_speed=-0.3, columns_speed=0):
    """Display animation of gun shot, direction and speed can be specified."""

    row, column = start_row, start_column

    canvas.addstr(round(row), round(column), '*')
    await asyncio.sleep(0)

    canvas.addstr(round(row), round(column), 'O')
    await asyncio.sleep(0)
    canvas.addstr(round(row), round(column), ' ')

    row += rows_speed
    column += columns_speed

    symbol = '-' if columns_speed else '|'

    rows, columns = canvas.getmaxyx()
    max_row, max_column = rows - 1, columns - 1

    curses.beep()

    while 0 < row < max_row and 0 < column < max_column:
        canvas.addstr(round(row), round(column), symbol)
        await asyncio.sleep(0)
        canvas.addstr(round(row), round(column), ' ')
        row += rows_speed
        column += columns_speed


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

    coroutines.append(fire(canvas,
                           row_max_canvas,
                           10,
                           ))

    while True:
        try:
            for coroutine in coroutines:
                coroutine.send(None)
            canvas.refresh()
            time.sleep(0.1)
        except StopIteration:
            break
        time.sleep(10)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
