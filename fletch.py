#!/Users/straateezy/anaconda/bin/python

import pickle
import nltk
from nltk.classify import NaiveBayesClassifier as nbc
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob.classifiers import NaiveBayesClassifier as nbcblob
from copy import deepcopy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import ne_chunk
from nltk import pos_tag
from nltk import word_tokenize
from nltk import chunk

'''
Loads the pickle for my 4283 labelled tweets (Key below).  Also, converts this
to another list, reversed_labelled_tweets_zip, which flips my (rank, tweet) tuples.

From here, tweets are stripped from stopwords, non-alphas and lowercased, tokenized, part-of-speech tagged,
stripped of proper nouns (NPP are replaced with 'blah') and finally the re-assembled tweets with corresponding
hand-labellings to final_preprocessed_tweet_and_classification.

Key:
0 = Injury-related
1 = Non-injury related incident effecting the game
2 = Irrelevant tweets
-----


'''

final_preprocessed_tweet_and_classification = []

keep_chars = ['(', ')']
gowords_lst = ['not play', 'out', 'out tonight', 'inactive', 'inactives', 'not return',
              'questionable', 'game to game', 'injury', 'injured', 'sore', 'broken',
              'hamstring', 'ACL']

stopwords_lst = stopwords.words('english')
stopwords_to_remove = ['out', 'isn', 'not']
for stopword in stopwords_to_remove:
    stopwords_lst.remove(stopword)

def openpickle():
    with open('/Users/straateezy/Notebooks/labelledzip.pkl', 'r') as picklefile1:
        labelled_tweets_zip = pickle.load(picklefile1)
        return labelled_tweets_zip


def converttweets(labelled_tweets_zip):
    reversed_labelled_tweets_zip = []
    for item in labelled_tweets_zip:
        reversed_labelled_tweets_zip.append((item[1], item[0]))
    return reversed_labelled_tweets_zip
    print 'returned reversed list'


def preprocesstokenize(reversed_labelled_tweets_zip):
    print len(reversed_labelled_tweets_zip)
    for tweet, category in reversed_labelled_tweets_zip:
        tokens = word_tokenize(tweet)
        classification = category
        tokens_tagged = pos_tag(tokens)
        create_new_list(classification, tokens_tagged)

def create_new_list(classification, tokens_tagged):
    tweet_lst = []
    for token in tokens_tagged:
        word_tweeted_tagged_token = token[0]
        grammatical_type_of_word = token[1]
        if word_tweeted_tagged_token.lower() in stopwords_lst:
            continue
        elif grammatical_type_of_word == 'NNP':
            tweet_lst.append('blah')
        elif word_tweeted_tagged_token.isalpha() or word_tweeted_tagged_token in keep_chars:
            tweet_lst.append(word_tweeted_tagged_token)
    string_of_tweet_lst = ' '.join(tweet_lst).lower()
    build_final_processed_list(string_of_tweet_lst, classification)

def build_final_processed_list(string_of_tweet_lst, classification):
    # FPTC = []
    # FPTC.append((string_of_tweet_lst, classification))
    final_preprocessed_tweet_and_classification.append((string_of_tweet_lst, classification))
    if len(final_preprocessed_tweet_and_classification) % 50 == 0:
        print 'finished processing tweet string: {}'.format(len(final_preprocessed_tweet_and_classification))

def outpickle(final_preprocessed_tweet_and_classification):
    with open('/Users/straateezy/atom/Fletcher/processed_labelled_list.pkl', 'w') as picklefile2:
        pickle.dump(final_preprocessed_tweet_and_classification, picklefile2)
        print 'dumping to pickle'
    # with open('/Users/straateezy/atom/Fletcher/processed_labelled_list_backup.pkl', 'w') as picklefile3:
    #     pickle.dump(backup, picklefile3)
    #     print 'dumping to pickle backup'

def main():
    # print final_preprocessed_tweet_and_classification[:100]
    labelled_tweets_zip = openpickle()
    for x in labelled_tweets_zip:
        if x[0] < 2:
            print x
    # reversed_labelled_tweets_zip = converttweets(labelled_tweets_zip)
    # preprocesstokenize(reversed_labelled_tweets_zip)
    # outpickle(final_preprocessed_tweet_and_classification)

if __name__ == '__main__':
    main()
