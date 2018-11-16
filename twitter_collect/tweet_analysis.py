import numpy as np
import matplotlib.pyplot as plt
from tweet_collection import *
from recup_tweet import *
tweets=collect()
data=make_dataframe(tweets)
print(data)

def more_likes(data):
    #à partir d'un tableau de tweets, récupère le tweet avec le + de like
    likes_max=np.max(data['likes'])
    #Récupère la ligne complète correspondant à ce tweet
    max_like= data[data.likes == likes_max].index[0]
    print("The tweet with more likes is: \n{}".format(data['Tweet'][max_like]))
    print("Number of likes: {}".format(max_like))

def more_RT(data):
    rt_max = np.max(data['RT'])
    rt  = data[data.RT == rt_max].index[0]
    #à partir d'un tableau de tweets, récupère le tweet avec le + de like
    print("The tweet with more retweets is: \n{}".format(data['Tweet'][rt]))
    print("Number of retweets: {}".format(rt_max))

print(more_likes(data))


###on fait une série avec les différents nb de likes pour les différents dates, idem avec les RT
tfav = pd.Series(data=data['likes'].values, index=data['Date'])
tret = pd.Series(data=data['RT'].values, index=data['Date'])

# Likes vs retweets visualization:
tfav.plot(figsize=(16,4), label="likes", legend=True)
tret.plot(figsize=(16,4), label="Retweets", legend=True)

plt.show()
