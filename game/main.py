import asyncio
import curses
import random
import time

from animation import animate_spaceship, fly_garbage

import os

path_to_folder = 'game/garbage'

all_files = os.listdir(path_to_folder)

GARBAGE = []
for file in [file_name for file_name in all_files if file_name.endswith('.txt')]:
    with open(f'{path_to_folder}/{file}', 'r') as f:
        GARBAGE.append(f.read())


async def blink(canvas, row, column, symbol='*', max_delay=4, offset_tics=(2, 1, 2, 4)):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        for _ in range(offset_tics[0]):  # now, with no random delay all stars blink synchronously!
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(offset_tics[1]):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        for _ in range(offset_tics[2]):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(offset_tics[3]):
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

    coroutines.append(fly_garbage(
        canvas,
        column=3,
        garbage_frame=GARBAGE[0],
    ))

    while True:
        for coroutine in coroutines.copy():  # now its don't missed coroutines?
            try:
                coroutine.send(None)
            except RuntimeError:
                coroutines.remove(coroutine)
            except StopIteration:
                continue
        canvas.refresh()
        time.sleep(0.1)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
