
import map
import reader

def main():
    tmp = reader.Reader()
    tmp_file = tmp.readerStr("./map/01.txt", "r")
    print(tmp_file)
    map.main(tmp_file)

if __name__ == "__main__":
    main = main()