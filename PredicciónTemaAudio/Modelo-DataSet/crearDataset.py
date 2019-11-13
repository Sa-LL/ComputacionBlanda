
import pickle

def crearDataset():
    dataset = []
    errores = 0
    for carpeta in ["deportes", "entretenimiento", "negocios", "politica", "tecnologia"]:
        limite = 0
        clase = 0
        if carpeta == "deportes":
            limite = 511
            clase = 0
        elif carpeta == "entretenimiento":
            limite = 387
            clase = 1
        elif carpeta == "negocios":
            limite = 511
            clase = 2
        elif carpeta == "politica":
            limite = 418
            clase = 3
        elif carpeta == "tecnologia":
            limite = 401
            clase = 4

        for number in range(1, limite):
            name = ""
            if number < 10:
                name = "t00" + str(number) + ".txt"
            elif number < 100:
                name = "t0" + str(number) + ".txt"
            else:
                name = "t" + str(number) + ".txt"
        


            with open(carpeta + "/" + name, "r", encoding="utf-8") as f:
                try:
                    text = f.read()
                    dataset.append([text, clase])
                except Exception as e:
                    errores += 1
                    print("error", errores, str(e))
                    
                    continue
    with open("dataSet.txt", "wb") as fp:   #Pickling
        pickle.dump(dataset, fp)

    print(len(dataset))


if __name__ == "__main__":
    crearDataset()    