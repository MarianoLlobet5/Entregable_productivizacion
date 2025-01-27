import pickle
import sklearn
import xgboost
def analizar_texto(texto_analizar):
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
    
    def tokenizado_stopwords(texto):
        texto = texto.lower()
        palabras = word_tokenize(texto)
        stop_words = set(stopwords.words('english'))
        palabras_filtradas = []
        for i in palabras:
            if i not in stop_words and i not in [".", ",", ":", ";", " ", "(", ")", "’", "“", "”", "@", "?", "-", "—", "_"] and i not in string.punctuation:
                palabras_filtradas.append(i)
        return ' '.join(palabras_filtradas)
    
    texto_analizar_tokenizado = tokenizado_stopwords(texto_analizar)
    
    from sklearn.feature_extraction.text import TfidfVectorizer
    import xgboost as xgb
    from xgboost import XGBClassifier
    
    texto_vectorizado = tfidf_vectorizer.transform([texto_analizar_tokenizado])
    prediccion = xgboost_model.predict(texto_vectorizado)
    
    # Devuelve la predicción como resultado
    return "La información que usted ha consultado es probablemente verdadera" if prediccion == 0 else "La información que usted ha consultado es probablemente falsa"
