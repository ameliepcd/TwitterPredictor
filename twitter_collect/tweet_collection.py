import json

import pandas as pd


def store_tweet(tweets,file_name):
    #prend en entrée le résultat d'une recherche API
    #On garde pour chacun le tweet, le hashtag, la date, à quel candidat il renvoie, l'ID du tweet
    #Création d'un fichier fait d'une liste de dico contenant les différents tweets
    T=[]
    for tweet in tweets:
        current_tweet={}
        current_tweet['tweet']=tweet.text
        current_tweet['Date']=str(tweet.created_at)
        current_tweet['User_ID']=tweet.id
        current_tweet['reply']=tweet.in_reply_to_status_id
        current_tweet['likes']=tweet.favorite_count
        T.append(current_tweet)

    #enregistrement du fichier dans le disque dur sous le nom de file_name
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(T,f)


from twitter_connection_setup import *

#####Renvoie une liste de tweet
def collect3():
    connexion = twitter_setup()
    tweets = connexion.search("Emmanuel Macron",language="french",rpp=1)
    liste_tweets=[]
    #Créer une liste des tweets correspondant à la collecte : on a donc une liste de dictionnaire
    for tweet in tweets :
        liste_tweets.append(tweet)

    return liste_tweets



def make_dataframe(status):
    #Status est le résultat d'une recherche API
    Tweet=[]
    Date=[]
    User_ID=[]
    Likes=[]
    RT=[]
    #### Création et remplissage des colonnes du futur tableau à partir des tweets donnés
    for tweet in status:
        Tweet.append(tweet.text)
        Date.append(str(tweet.created_at))
        User_ID.append(tweet.id)
        Likes.append(int(tweet.favorite_count))
        RT.append(int(tweet.retweet_count))
    ###Création du tableau avec les colonnes formées avant
    S=pd.DataFrame({'Tweet': Tweet ,
                    'Date': Date  ,
                    'User_ID': User_ID,
                    'likes': Likes,
                    'RT': RT})
    return(S)

###TEST

#store_tweet(tweets,'test_1_EmmanuelMacron')


