import curses
import time

def main(list):

    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()

    stdscr.keypad(True)

    while True:
        try:
            entry = stdscr.getch()
            stdscr.clear()
            h, w = stdscr.getmaxyx()
            i = 0
            for x in list:
                stdscr.addstr(i, 0, x)
                i+= 1
                stdscr.refresh()

#             test = curses.ascii.ctrl('P')
            if entry == curses.KEY_UP:
                stdscr.addstr(10, 10, 'test')
            if entry == curses.KEY_DOWN:
                stdscr.addstr(10, 10, "je suis sur la touche du bas")
            if entry == curses.KEY_LEFT:
                stdscr.addstr(10, 10, "je suis sur la touche de gauche")
            if entry == curses.KEY_RIGHT:
                stdscr.addstr(10, 10, "je suis sur la touche de droite")
            if entry == 32:
                stdscr.refresh()
            if entry == 27:
                raise error
            if entry == 81:
                raise error

        except error:
                raise KeyboardInterrupt
        except:
            return ('error')

    curses.endwin()

if __name__ == "__main__":

    curses.wrapper(main)