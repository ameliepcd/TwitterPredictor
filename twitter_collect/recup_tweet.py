from twitter_collect.twitter_connection_setup import *

#On donne la liste des recherches de tweets à faire
liste_query=['Emmanuel Macron','Emmanuel','Macron','Emmanuel AND Macron','#EnMarche','Brigitte AND Macron','Brigitte AND Emmanuel']

def collect(queries):
    connexion = twitter_setup()
    liste_tweets=[]
    for i in range (len(liste_query)):
        tweets = connexion.search(queries[i],language="french",rpp=50)

    #Créer une liste des tweets correspondant à la collecte : on a donc une liste de dictionnaire
        for tweet in tweets :
            liste_tweets.append(tweet)

    return liste_tweets


def collect_by_user(user_id):
    connexion = twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 200)
    for status in statuses:
        print(status.text)


#print(collect_by_user(''))

print(collect(liste_query))
