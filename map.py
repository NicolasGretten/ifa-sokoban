import curses
import time
import re

def main(lines, P, O, X, limit):

    player = P

    boulder = O

    position = X

    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()

    counter = 0

    stdscr.keypad(True)

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
                counter +=1
                player[0] -=1
                player[1] = player[1]
                stdscr.addstr(player[0], player[1], "P")
                stdscr.addstr(10, 10, f"nombre de coup : {counter}")

            if entry == curses.KEY_DOWN:
                counter +=1
                player[0] +=1
                player[1] = player[1]
                stdscr.addstr(player[0], player[1], "P")
                stdscr.addstr(10, 10, f"nombre de coup : {counter}")

            if entry == curses.KEY_LEFT:
                counter +=1
                player[0] = player[0]
                player[1] -= 1
                stdscr.addstr(player[0], player[1], "P")
                stdscr.addstr(10, 10, f"nombre de coup : {counter}")

            if entry == curses.KEY_RIGHT:
                counter +=1
                player[0] = player[0]
                player[1] += 1
                stdscr.addstr(player[0], player[1], "P")
                stdscr.addstr(10, 10, f"nombre de coup : {counter}")

            #Espace
            if entry == 32:
                player[0] = P[0]
                player[1] = P[1]
                counter = 0
#                 stdscr.refresh()

            #Echap
            if entry == 27:
                raise error

            #Q
            if entry == 81:
                raise error

        except error:
                raise KeyboardInterrupt
        except:
            return ('error')

    curses.endwin()

if __name__ == "__main__":

    curses.wrapper(main)