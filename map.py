import curses
import time
import collections

def map(map, P, O, X, limit):

    #le player
    player = P
    hasBox = False

    #la box
    _box = O

    #l'emplacement
    _emplacement = X

    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()

    #compteur de coup
    counter = 0

    stdscr.keypad(True)

    while True:
        try:
            entry = stdscr.getch()
            stdscr.clear()

            i = 0

            #génération de la map depuis
            for line in map:
                stdscr.addstr(i, 0, line)
                i+= 1
                stdscr.refresh()

            stdscr.addch(O[0], O[1], "O")

            #Déplacement
            if entry == curses.KEY_UP:
                counter +=1
                player[0] -=1
                player[1] = player[1]

                if player in limit:
                    player[0] +=1
                    player[1] = player[1]
                    stdscr.addstr(player[0], player[1], "P")
                    stdscr.addstr(0,2, f"Vous foncez dans le mur ! nombre de coup : {counter}")
                else :
                    stdscr.addstr(player[0], player[1], "P")
                    stdscr.addstr(0,2, f"nombre de coup : {counter}")

            if entry == curses.KEY_DOWN:
                counter +=1
                player[0] +=1
                player[1] = player[1]
                if player in limit:
                     player[0] -=1
                     player[1] = player[1]
                     stdscr.addstr(player[0], player[1], "P")
                     stdscr.addstr(0,2, f"Vous foncez dans le mur ! nombre de coup : {counter}")
                else :
                     stdscr.addstr(player[0], player[1], "P")
                     stdscr.addstr(0,2, f"nombre de coup : {counter}")

            if entry == curses.KEY_LEFT:
                counter +=1
                player[0] = player[0]
                player[1] -= 1
                if player in limit:
                    player[0] = player[0]
                    player[1] +=1
                    stdscr.addstr(player[0], player[1], "P")
                    stdscr.addstr(0,2, f"Vous foncez dans le mur ! nombre de coup : {counter}")
                else :
                    stdscr.addstr(player[0], player[1], "P")
                    stdscr.addstr(0,2, f"nombre de coup : {counter}")

            if entry == curses.KEY_RIGHT:
                counter +=1
                player[0] = player[0]
                player[1] += 1
                if player in limit:
                    player[0] = player[0]
                    player[1] -=1
                    stdscr.addstr(player[0], player[1], "P")
                    stdscr.addstr(0,2, f"Vous foncez dans le mur ! nombre de coup : {counter}")
                else :
                    stdscr.addstr(player[0], player[1], "P")
                    stdscr.addstr(0,2, f"nombre de coup : {counter}")

            #Condition
            if player == _box and hasBox == True:
                stdscr.addstr(0,2, "Vous avez déjà récupérer cette boite")
                stdscr.refresh()

            if player == _box and hasBox == False:
                hasBox = True
                stdscr.addstr(0,2, "Vous avez récupérer une boite")
                stdscr.refresh()

            if player == _emplacement and hasBox == True:
                stdscr.addstr(0,2, "Vous avez Gagner !! Espace pour recommencer")
                stdscr.keypad(False)

            #Entrer utilisteur pour reload ou quitter
            if entry == 32:
                counter = 0
                stdscr.keypad(True)
                stdscr.clear()
                stdscr.refresh()
                player[0] = P[0]
                player[1] = P[1]

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