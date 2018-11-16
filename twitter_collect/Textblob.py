from tweet_collection import *
from textblob import TextBlob
from textblob import Word


def collect2():
    connexion = twitter_setup()
    tweets = connexion.search("Emmanuel Macron",language="french",rpp=1)
    liste_tweets=[]
    #Créer une liste des textes des tweets
    for tweet in tweets :
        liste_tweets.append(tweet.text)

    return liste_tweets


def voc(tweets):
    text=''
    #à partir d'une liste de réponse d'API, récupère le texte des tweets dans dans une liste
    text=''
    for tweet in tweets:
        text+=tweet.text
    liste=TextBlob(text)
    wordlist=liste.words
    unique=[]
    for word in wordlist:
        w=Word(word)
        #on récupère les tweets en forme de base, plus long que 2 lettres et pas trop fréquents
        if w==w.lemmatize() and len(w)>2 and liste.word_counts[w]<=5 :
            unique.append(w)
    return(unique)

###A FINIR

#print(tweets)

#tweets=collect()
#print(voc(tweets))

from textblob.en import sentiment as pattern_sentiment
from textblob.tokenizers import word_tokenize
from textblob.decorators import requires_nltk_corpus
from textblob.base import BaseSentimentAnalyzer, DISCRETE, CONTINUOUS



#def opinion(tweet):
    #prend en entrée le résultat d'une recherche API concernant un candidat


def analize_sentiment(tweets):
    '''
    Donne le sentiment d'un tweet donné
    '''
    pos=[]
    neg=[]
    neu=[]
    for tweet in tweets:
        analysis = TextBlob(tweet)
        #On regarde pour chaque tweet, si il est positif au négatif, sachant que l'échelle
        # va de 1 (positif)à -1 (négatif)

        if analysis.sentiment.polarity > 0.2:
            pos.append(analysis.sentiment.polarity)
        elif analysis.sentiment.polarity < -0.2:
            neg.append(analysis.sentiment.polarity)
        else:
            neu.append(analysis.sentiment.polarity)
    print("Percentage of positive tweets: {}%".format(len(pos)*100/len(tweets)))
    print("Percentage of neutral tweets: {}%".format(len(neu)*100/len(tweets)))
    print("Percentage de negative tweets: {}%".format(len(neg)*100/len(tweets)))

#analize_sentiment(collect2())



