import asyncio
import curses
from curses_tools import draw_frame


with open('./game/rocket_frames/rocket_frame_1.txt', 'r') as f:
    FRAME_1 = f.read()

with open('./game/rocket_frames/rocket_frame_2.txt') as f:
    FRAME_2 = f.read()


async def animate_spaceship(canvas: curses.window,
                            start_row: int,
                            start_column: int,
                            rows_speed=-0.3,
                            columns_speed=0) -> None:
    """Animate spaceship movement"""

    while True:
        draw_frame(canvas, start_row, start_column, FRAME_1)
        await asyncio.sleep(0)

        draw_frame(canvas, start_row, start_column, FRAME_1, negative=True)
        draw_frame(canvas, start_row, start_column, FRAME_2)
        await asyncio.sleep(0)
        draw_frame(canvas, start_row, start_column, FRAME_2, negative=True)



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


if __name__ == '__main__':
    print(FRAME_1, FRAME_2, sep='\n')
