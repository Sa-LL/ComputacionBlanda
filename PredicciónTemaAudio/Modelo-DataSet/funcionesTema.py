import spacy 
import spacy.lang.es as es 
from spacy.lang.es import Spanish
import string
punctuations = string.punctuation
stopwords_es = list(es.STOP_WORDS)
import spacy 
import spacy.lang.es as es
parser = Spanish()
from spacy.lang.es import Spanish
def quitarSimbolos(listText):
    SYMBOLS = '}{()[].,:;+-*/#%\&|<>=~$1234567890'
    for index in range(len(listText)):
        for symbol in SYMBOLS:
            listText[index] = listText[index].replace(symbol, "")
        
    newList = [item.translate(SYMBOLS).strip() for item in listText]
    return newList

def quitarTildes(text):
    text = text.replace("á", "a")
    text = text.replace("é", "e")
    text = text.replace("í", "i")
    text = text.replace("ó", "o")
    text = text.replace("ú", "u")
    text = text.replace("ñ", "n")
    return text

def tokenizador(text):  
    text = quitarTildes(text) #Solo espaniol
    text = text.replace("\r", " ")
    text = text.replace("\n", " ")
    text = text.replace("    ", " ")
    text = text.replace('"', '')
    text = text.replace("''", '')
    text = text.replace("'s", "")
    tokens = parser(text)
    tokens = [word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in tokens]
    quitarSimbolos(tokens)
    #tokens  = [t for t in tokens if not isinstance(t, str)]
    tokens = [word for word in tokens if word not in stopwords_es and word not in punctuations]
    text = " ".join(tokens)
    return text


def tag_to_theme(number):
    if number == 0:
        return "deportes"
    elif number == 1:
        return "entretenimiento"
    elif number == 2:
        return "negocios"
    elif number == 3:
        return "politica"
    else:
        return "tecnologia"
        
#print(tokenizador("Hola, mi nombre es david cediel y tengo 21 años"))