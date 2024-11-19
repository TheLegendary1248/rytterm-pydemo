import curses
def main(stdscr): 
    stdscr.clear()
    # curses.noecho()
    # curses.cbreak()
    for i in range(0,9):
        stdscr.addch(i,i,"┌") 
    stdscr.refresh()
    stdscr.getkey()
curses.wrapper(main)
