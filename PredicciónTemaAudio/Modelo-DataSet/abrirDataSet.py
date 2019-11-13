import pickle

def abrirDataset():
    with open("dataSet.txt", "rb") as fp:   # Unpickling
        b = pickle.load(fp)
        print(b[:10,1])


if __name__ == "__main__":
    abrirDataset()