import os

class Reader:
    def __init__(self):
        pass

    def readerStr(self, path, mode):
        assert mode in ['r', 'rb', 'rb+'], 'Les modes disponibles sont r, rb, rb+'
        assert os.path.exists(path), 'Le fichier n existe pas'
        print('test')
        with open(path, mode) as file:
            return file.readlines()
            # for line in file:


