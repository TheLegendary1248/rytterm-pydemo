import curses
def main(stdscr):
    stdscr.clear()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    tui = curses.newwin(5,5,0,0)
    tui.addch(1,1,'$')
    tui.refresh()
curses.wrapper(main)
