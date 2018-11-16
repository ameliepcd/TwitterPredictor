#On recupère tous les tweets des membres de l'équipe du candidat et du candidat par leurs noms d'utilisateurs
## On récupère tous les RT et les Reply des tweets des candidates et son équipe

from twitter_connection_setup import *
from recup_tweet import *

def get_replies(user_id):
   connexion = twitter_setup()
   replies=[]
    #recupere les messages recents du candidat  user_id
   for full_tweet in connexion.user_timeline(id = user_id,language="fr",rpp=100):
       print(full_tweet.text)
       #query pour retrouver des tweets repondant a l'utilisateur used_id
       query = 'to:'+user_id
       print(query)

       for tweet in connexion.search(q=query, since_id=992433028155654144, result_type='recent',timeout=999999):
           print(tweet.text)
            #si le tweet renvoye par la requete possede un champs "in reply_to__status_id_str" cest a dire si cest une reponse a un tweet
           if hasattr(tweet, 'in_reply_to_status_id_str'):
                # si c'ets une reponse au tweet actuel (full_tweet) du candidat
               if (tweet.in_reply_to_status_id_str==full_tweet.id_str):
                   replies.append(tweet.text)
                   print(tweet.text)

#print(get_replies('EmmanuelMacron'))

#Pour un nom de candidat donné, affiche les tweets du candidats
def get_retweets_of_candidate(num_candidate):
    connexion = twitter_setup()
    statuses = connexion.user_timeline(id = num_candidate, count = 200)
    tweet_du_candidat=[]

    #On crée la liste des tweets du candidat concerné
    for status in statuses:
        tweet_du_candidat.append(status.text)

    #Pour chacun des tweets du candidats, on l'imprime et on affiche après les RT
    for i in range (len(tweet_du_candidat)):
        tweets = connexion.search(tweet_du_candidat[i],language="french",rpp=50)
        print(tweet_du_candidat)
        for tweet in tweets:
            print(tweet.text)

#print(get_retweets_of_candidate('EmmanuelMacron'))





