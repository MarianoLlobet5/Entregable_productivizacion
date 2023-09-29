import pickle
import sklearn
import xgboost
# Cargar modelos desde el archivo pickle
with open("modelos_entrenados.pkl", 'rb') as file:
    modelos_cargados = pickle.load(file)
# Acceder a modelos individuales
tfidf_vectorizer = modelos_cargados["Tfid_vectorizer"]
xgboost_model = modelos_cargados["XGBoost"]
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
import string
def tokenizado_stopwords (texto):
    texto = texto.lower() #lo pasamos a minúsculas
    palabras = word_tokenize(texto) #tokenizado del texto
    stop_words = set(stopwords.words('english')) #cargamos el set de stopwords en inglés
    #eliminamos las stopwords del texto tokenizado
    palabras_filtradas = []
    for i in palabras:
        if i not in stop_words and i not in [".",",",":",";"," ","(",")","’","“","”","@","?","-","—","_"] and i not in string.punctuation : #He intentado eliminar todos los caracteres que pueda haber en el texto y que no sean palabras
            palabras_filtradas.append(i)
    return ' '.join(palabras_filtradas)
texto_mariano_prueba = "Most U.S. national parks will close if the government shuts down, federal officials said."
texto_mariano_tokenizado = tokenizado_stopwords(texto_mariano_prueba)
from sklearn.feature_extraction.text import TfidfVectorizer
import xgboost as xgb
from xgboost import XGBClassifier  # Para clasificación
texto_vectorizado = tfidf_vectorizer.transform([texto_mariano_tokenizado])
prediccion = xgboost_model.predict(texto_vectorizado)
print(prediccion)
