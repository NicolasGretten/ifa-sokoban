
import map
import reader

def main():
    tmp = reader.Reader()
    tmp_file = tmp.readerStr("./map/01.txt", "r")
    print(tmp_file)

    limit = []
    i = 0
    coordP = []
    coordO = []
    coordX = []

    for line in tmp_file:
        coor = [i, len(line) -1]
        limit.append(coor)

        PlayerYPosition = line.find("P")

        if line.find("P") != -1:
            coordP = [i, line.find("P")]

        if line.find("O") != -1:
            coordO = [i, line.find("O")]

        if line.find("X") != -1:
            coordX = [i, line.find("X")]

        i+= 1

    map.main(tmp_file,coordP, coordO, coordX, limit)


    print(limit, coordP, coordO, coordX)
if __name__ == "__main__":
    main = main()