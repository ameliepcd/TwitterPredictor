#on récupère les tweets sur un candidat et sur son équipe en direct :
# avec l'API STREAMING

def get_tweets_from_candidates_search_queries(queries):
    connexion = twitter_setup()
    for i in range (len(queries)):
        tweets = connexion.search(queries[i],language="french",rpp=100)
        for tweet in tweets:
            print(tweet.text)


