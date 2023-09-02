from Tarea1 import *

tweet1="Excelente en su área, su muerte es una enorme pérdida y debería ser luto nacional!!!"
tweet2="A pesar de la pérdida que sentimos por la muerte de nuestro ser querido, encontramos consuelo en los momentos positivos que compartimos juntos, recordando su gran amor y su excelente sentido del humor."
tweet3="El luto que experimentamos por la partida de nuestro amigo es abrumador, pero nos esforzamos por mantener una perspectiva positiva, recordando las excelentes experiencias que compartimos y el gran impacto que tuvo en nuestras vidas."
tweet4="Aunque enfrentamos la tristeza de la pérdida, buscamos el lado positivo al celebrar la vida de nuestro ser querido. Su legado es una muestra excelente de cómo una persona puede dejar un gran impacto en el mundo a través de sus acciones y bondad"


palabras_clave = ["muerte", "pérdida", "luto", "excelente","gran" , "positivo"]

positivas = ["excelente","gran",  "positivo"]
neutras = ["pérdida"]
negativas = ["muerte", "luto"]
score = [1,0,-1]


tweets = [tweet1, tweet2, tweet3, tweet4]
mas_positivo = tweet_mas_positivo(tweets, positivas, neutras, negativas)
mas_negativo = tweet_mas_negativo(tweets, positivas, neutras, negativas)
promedio_de_calidades = calidad_promedio(tweets, palabras_clave)

print("el tweet mas positivo es: ", mas_positivo)
print("El tweet mas negtivo es: ", mas_negativo)
print("La calidad promedio de los tweets:  ", promedio_de_calidades)