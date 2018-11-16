from collect_candidate_actuality_tweets import *
from collect_candidate_tweet_activity import *
from Get_Queries import *
from Prise_en_main import *
from tweet_collect_whole import *
from twitter_connection_setup import *

hashtag_1=get_candidate_queries('hashtag_candidate_1.txt')
hashtag_2=get_candidate_queries('hashtag_candidate_2.txt')
keywords_1=get_candidate_queries('keywords_candidate_1.txt')
keywords_2=get_candidate_queries('keywords_candidate_2.txt')

candidat1=hashtag_1+keywords_1
candidat2=hashtag_2+keywords_2

#Pour chaque candidat et les demandes du clients associés, il retourne les réponses
# des différentes fonctions créées avant.
def collect(num_candidate,queries):
    connexion= twitter_setup()
    candidat_RT=get_retweets_of_candidate(num_candidate)
    tweet_about_candidate=get_tweets_from_candidates_search_queries(queries)
    candidate_replies=get_replies(num_candidate)
    return(candidat_RT,tweet_about_candidate,candidate_replies)



