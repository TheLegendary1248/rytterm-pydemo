#src: 
from threading import Thread
import curses
import time
import os
key_pressed = False

def detect_key_press():
    global key_pressed
    stdscr = curses.initscr()
    key = stdscr.getch()
    key_pressed = True
    exit()

def main():
    thread = Thread(target = detect_key_press)
    thread.start()
    while not key_pressed:
        time.sleep(0.5)
        print("Heck!\r")

def exit():
    curses.endwin()
    os._exit(0)

main()
