
import map
import reader
import re

class playerError(Exception):
    pass

class boulderError(Exception):
    pass

def main():
    try:
        tmp = reader.Reader()
        tmp_file = tmp.readerStr("./map/01.txt", "r")
        map_file = []

        i = 0
        counterP = 0
        counterX = 0
        counterO = 0

        coordP = []
        coordO = []
        coordX = []
        coordLimit = []

        for line in tmp_file:
            coor = [i, len(line) -1]

            if line.find("P") != -1:
                counterP += 1
                coordP = [i, line.find("P")]
                line = line.replace('P', ' ')

            if line.find("O") != -1:
                counterO += 1
                coordO = [i, line.find("O")]
                line = line.replace('O', ' ')

            if line.find("X") != -1:
                counterX += 1
                coordX = [i, line.find("X")]

            if line.find("#") != -1:
                res = [i for i in range(len(line)) if line.startswith("#", i)]
                for y in res:
                    coordLimit.append([i, y])

            i+= 1

            map_file.append(line)

        if counterP > 1:
            raise playerError
        if counterO != counterX:
            raise boulderError

        map.map(map_file, coordP, coordO, coordX, coordLimit)

    except boulderError:
        print('le nombre de box et d\'emplacement ne sont pas les mêmes.')
    except playerError:
        print('pas plus de un joueur autorisé.')

if __name__ == "__main__":
    main = main()