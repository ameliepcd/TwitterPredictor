#API SEARCH


from twitter_connection_setup import *
def collect():
    connexion = twitter_setup()
    tweets = connexion.search("Emmanuel Macron",language="french",rpp=100)
    for tweet in tweets:
        print(tweet)

#print(collect())
#-> affiche les tweets relatifs à un mot clé, ici avec Emmanuel Macron en français avec au max 100 tweets

#API USERS

def collect_by_user(user_id):
    connexion = twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 200)
    for status in statuses:
        print(status.text)
    return statuses

#-> affiche tous les tweets d'une personne, et au max 200

#API Streaming
#->  Si les clients dépassent un nombre limité de tentatives de connexion à l'API de
# diffusion en continu dans une fenêtre temporelle, ils recevront l'erreur 420.
# Ensuite, on peut filtrer les tweets cherchés


from textblob import TextBlob

from tweepy.streaming import StreamListener
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        if  str(status) == "420":
            print(status)
            print("You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True


def collect_by_streaming():

    connexion = twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener=listener)
    stream.filter(track=['Emmanuel Macron'])

#print(collect_by_user('Marsattacks23'))


#monty = TextBlob("We are no longer the Knights who say Ni. "
#                    "We are now the Knights who say Ekki ekki ekki PTANG.")
#print(monty.word_counts['ekki'])
