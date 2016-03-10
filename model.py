import pickle
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.feature_extraction.text import TfidfVectorizer

'''
Takes the proc_labl_tweets we created in fletcher.py and turns them into two
dictionaries with corresponding indicies as keys.  Then, converts these into
two lists; checking for identical lengths.  Next, we build our MultinomialNB
model and our vectorizer.  We fit the model and are ready to predict.

'''


def openpickle():
    with open('/Users/straateezy/atom/Fletcher/processed_labelled_list.pkl', 'r') as picklefile:
        proc_labl_tweets = pickle.load(picklefile)
        return proc_labl_tweets

# def separate_PLT(proc_labl_tweets):
#     idx_tweet_dict = {}
#     idx_category_dict = {}
#     for idx, tweet, category in enumerate(proc_labl_tweets):
#         idx_tweet_dict[idx] = tweet
#         idx_category_dict[idx] = category
#     return idx_tweet_dict, idx_category_dict
#
# def make_xy_train(idx_tweet_dict, idx_category_dict):
#     x_train = []
#     y_train = []
#     if len(idx_tweet_dict) != len(idx_category_dict):
#         print 'Something is wrong; tweet and cat dicts diff lengths'
#     for x in range(len(idx_tweet_dict)):
#         x_train.append(idx_tweet_dict[x])
#         y_train.append(idx_category_dict[x])
#     if len(x_train) != len(y_train):
#         print 'Something is wrong; x and y train diff lengths'
#     return x_train, y_train
#
# def build_MNBC_model(x_train, y_train):
#     clf = MultinomialNB()
#     vectorizer = TfidfVectorizer(ngram_range=(1,3))
#     x_train_vec_trans = vectorizer.fit_transform(x_train)
#     clf.fit(x_train_vec_trans, y_train)
#     print clf.predict(vectorizer.transform(['injury tonight, john is out']))
#
#
# def pickle_output_train(x_train, y_train):
#     with open('x_train.pkl', 'w') as picklefileout:
#         picklefileout.dump(x_train, picklefileout)
#     with open('y_train.pkl', 'w') as picklefileout2:
#         picklefileout2.dump(y_train, picklefileout2)

def main():
    proc_labl_tweets = openpickle()
    print proc_labl_tweets
    # idx_tweet_dict, idx_category_dict = separate_PLT(proc_labl_tweets)
    # x_train, y_train = make_xy_train(idx_tweet_dict, idx_category_dict)
    # build_MNBC_model(x_train, y_train)


if __name__ == '__main__':
    main()
