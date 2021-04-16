import curses
import time

def main(lines, P, O, X, limit):

    player = P

    boulder = O

    position = X

    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()

    stdscr.keypad(True)

    curses.setsyx(P[0], P[1])

    while True:
        try:
            entry = stdscr.getch()
            stdscr.clear()
            h, w = stdscr.getmaxyx()
            i = 0

            for x in lines:
                stdscr.addstr(i, 0, x)
                i+= 1
                stdscr.refresh()

            if entry == curses.KEY_UP:
                player[0] -=1
                player[1] = player[1]
                stdscr.addstr(10, 10, f"{player[0]}, {player[1]} ")

            if entry == curses.KEY_DOWN:
                player[0] +=1
                player[1] = player[1]
                stdscr.addstr(10, 10, f"{player[0]}, {player[1]} ")

            if entry == curses.KEY_LEFT:
                player[0] = player[0]
                player[1] -= 1
                stdscr.addstr(10, 10, f"{player[0]}, {player[1]} ")

            if entry == curses.KEY_RIGHT:
                player[0] = player[0]
                player[1] += 1
                stdscr.addstr(10, 10, f"{player[0]}, {player[1]} ")

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