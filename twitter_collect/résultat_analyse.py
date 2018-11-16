import seaborn as sns
from textblob import *

sns.set(style="whitegrid")


results = sns.load_dataset('résultat_collection_sentiment')
#results doit être sous forme d'une dataframe

# Draw a nested barplot to show the repartition of neg,pos, and neu opinions for each candidate
g = sns.catplot(x="candidate", y="opinions", hue="type", data=results,
                height=6, kind="bar", palette="muted")
g.despine(left=True)
g.set_ylabels('repartition of opinions')
