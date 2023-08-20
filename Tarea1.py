import numpy as np
import pandas as pd

tweet1="Excelente en su área, su muerte es una enorme pérdida y debería ser luto nacional!!!"
tweet2="A pesar de la pérdida que sentimos por la muerte de nuestro ser querido, encontramos consuelo en los momentos positivos que compartimos juntos, recordando su gran amor y su excelente sentido del humor."
tweet3="El luto que experimentamos por la partida de nuestro amigo es abrumador, pero nos esforzamos por mantener una perspectiva positiva, recordando las excelentes experiencias que compartimos y el gran impacto que tuvo en nuestras vidas."
tweet4="Aunque enfrentamos la tristeza de la pérdida, buscamos el lado positivo al celebrar la vida de nuestro ser querido. Su legado es una muestra excelente de cómo una persona puede dejar un gran impacto en el mundo a través de sus acciones y bondad"


palabras_clave = ["muerte", "pérdida", "luto", "excelente","gran" , "positivo"]

positivas = ["excelente","gran",  "positivo"]
neutras = ["pérdida"]
negativas = ["muerte", "luto"]

def vector_palabras_clavas(tweet, palabras_clave):
    w = [0,0,0,0,0,0]
    
    for clave in palabras_clave:
        for word in tweet:
            if word.lower()==clave.lower():
                i = palabras_clave.index(clave)
                w[i] = 1
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
    x = np.array(w)
    largo = 1/len(w)
    return x*largo


def score_sentimental(s,v_score):
    #s = calidad(s)
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
        w = vector_palabras_clavas(w, palabras_clave)
        w = calidad(w)
        calidades += w
    return calidades/len(tweets)






# tweet = string_to_vector_palabras(tweet1)
# w1 = vector_palabras_clavas(tweet, palabras_clave)
# s1 = count_palabras_clave(tweet, positivas, neutras,negativas)
# cali1 = calidad(w1)
# score = [1,0,-1]
# total_score1 = score_sentimental(s1, score)

# tweet = string_to_vector_palabras(tweet2)
# w2 = vector_palabras_clavas(tweet, palabras_clave)
# s2 = count_palabras_clave(tweet, positivas, neutras,negativas)
# cali = calidad(w2)
# total_score2 = score_sentimental(s2, score)

# tweet = string_to_vector_palabras(tweet3)
# w3 = vector_palabras_clavas(tweet, palabras_clave)
# s3 = count_palabras_clave(tweet, positivas, neutras,negativas)
# cali3 = calidad(w3)
# total_score3 = score_sentimental(s3, score)

# tweet = string_to_vector_palabras(tweet4)
# w4 = vector_palabras_clavas(tweet, palabras_clave)
# s4 = count_palabras_clave(tweet, positivas, neutras,negativas)
# cali4 = calidad(w4)
# total_score4 = score_sentimental(s4, score)

# print(total_score1)
# print(total_score2)
# print(total_score3)
# print(total_score4)
tweets = [tweet1, tweet2, tweet3, tweet4]
mas_positivo = tweet_mas_positivo(tweets, positivas, neutras, negativas)
mas_negativo = tweet_mas_negativo(tweets, positivas, neutras, negativas)
promedio_de_calidades = calidad_promedio(tweets, palabras_clave)

print("el tweet mas positivo es: ", mas_positivo)
print("El tweet mas negtivo es: ", mas_negativo)
print("La calidad promedio de los tweets:  ", promedio_de_calidades)


