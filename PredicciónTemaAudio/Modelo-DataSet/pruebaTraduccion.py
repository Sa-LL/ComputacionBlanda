from googletrans import Translator

def traducir():
    
    for number in range(343, 402):
        translator = Translator() #Libreria google trans
        name = ""
        if number < 10:
            name = "00" + str(number) + ".txt"
        elif number < 100:
            name = "0" + str(number) + ".txt"
        else:
            name = str(number) + ".txt"
        #f = open(name, "r")
        #
        with open(name, "r") as f:
            text = f.read()
            #print("hola")
            try:
                text_traduced = translator.translate(text, src="en", dest="es") #Libreria google trans
            except:
                continue

            
        #print(text_traduced)

        name2 = "t" + name
        with open(name2, "w", encoding="utf-8") as f:
            f.write(text_traduced.text)
if __name__ == "__main__":
    traducir()