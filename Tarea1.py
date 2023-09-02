import numpy as np
import pandas as pd



def vector_palabras_claves(tweet, palabras_clave):
    w = [0] * len(palabras_clave)
    
    for clave in palabras_clave:
        for word in tweet:
            if word.lower()==clave.lower():
                i = palabras_clave.index(clave)
                w[i] += 1
    return w        

def count_palabras_clave(tweet, positivas, neutras, negativas):
    s = [0,0,0]
    for positiva in positivas:
        for word in tweet:
            if positiva.lower() == word.lower():
                s[0] += 1
    for neutra in neutras:
        for word in tweet:
            if neutra.lower() == word.lower():
                s[1] += 1
    for negativa in negativas:
        for word in tweet:
            if negativa.lower() == word.lower():
                s[2] += 1

    return s


def calidad(w):
    calidad = 0
    largo = 1/len(w)

    for cant in w:
        calidad = calidad + cant 
    return calidad*largo


def score_sentimental(s,v_score):
    
    v_score = np.array(v_score)
    return np.dot(v_score, s)

def string_to_vector_palabras(tweet):
    return tweet.replace("!","").replace(",","").replace(".","").split(" ") # split convierte cada  tweet en un vector por cada palabra


def tweet_mas_positivo(tweets, positivas, neutras, negativas):
    tweets_scores = []
    for tweet in tweets:
        s = string_to_vector_palabras(tweet)
        s = count_palabras_clave(s, positivas, neutras, negativas)
        s = score_sentimental(s,[1,0,-1])
        tweets_scores.append(s)

    positivo = max(tweets_scores)
    i = tweets_scores.index(positivo)
    return tweets[i]

def tweet_mas_negativo(tweets, positivas, neutras, negativas):
    tweets_scores = []
    for tweet in tweets:
        s = string_to_vector_palabras(tweet)
        s = count_palabras_clave(s, positivas, neutras, negativas)
        s = score_sentimental(s,[1,0,-1])
        tweets_scores.append(s)

    negativo = min(tweets_scores)
    i = tweets_scores.index(negativo)
    return tweets[i]


def calidad_promedio(tweets, palabras_clave):
    calidades = 0
    for tweet in tweets:
        w = string_to_vector_palabras(tweet)
        w = vector_palabras_claves(w, palabras_clave)
        w = calidad(w)
        calidades += w
    return calidades/len(tweets)








