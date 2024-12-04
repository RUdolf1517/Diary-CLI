#!/usr/bin/env python3

from lib_for_program import *
import curses
def main(stdscr):
    screen = curses.initscr()
    screen.refresh()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    menu = ['Add new task', 'See tasks', 'Delete task', 'Reset tasks', 'Edit task', 'Exit']
    current_row = 0
    while True:
        stdscr.clear()
        for idx, row in enumerate(menu):
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(idx, 0, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(idx, 0, row)

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:  # Enter key
            if current_row == 0:
                stdscr.clear()
                stdscr.addstr(0, 0, "test")
                stdscr.refresh()
                stdscr.getch()

            elif current_row == 1:
                read_new_tasks(stdscr)

            elif current_row == 5:
                break



curses.wrapper(main)




"""def motor():
    while True:
        messages()
        m = int(input("choose the command:"))
        choose(m)"""


#motor()
