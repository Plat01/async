import curses
import os
import time


os.environ['TERM'] = 'xterm-256color'


def draw(canvas: curses.window):
    row, column = (5, 20)
    canvas.addstr(row, column, str(type(canvas)))
    curses.curs_set(False)
    canvas.border()
    canvas.refresh()
    time.sleep(10)
    # while True:
    #     char = canvas.getch()
    #     print(char)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
