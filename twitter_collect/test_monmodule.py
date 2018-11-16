from __main__ import *
from pytest import *



def test_collect():
    tweets = collect(Macron,candidat1)
    data =  transform_to_dataframe(tweets)
    assert 'tweet_textual_content' in data.columns

print(test_collect())
