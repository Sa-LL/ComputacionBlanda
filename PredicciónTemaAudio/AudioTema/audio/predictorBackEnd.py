from joblib import load
from sklearn.feature_extraction.text import TfidfVectorizer
from .funcionesTema import tag_to_theme, tokenizador
import pickle



def analizar(texto):
    clf = load('C://Users//David Cediel//Desktop//bbc//traducido/modeloSpanish.joblib')
    tfidf = pickle.load(open("C://Users//David Cediel//Desktop//bbc//traducido/tfidf.pickle", "rb" ))
    textTokenized = tokenizador(texto)
    features_texto= tfidf.transform([textTokenized]).toarray()
    y = clf.predict(features_texto)
    return tag_to_theme(y)
    

if __name__ == "__main__":
   print( analizar("El equipo de futbol millonarios gano la final de la copa libertadores"))