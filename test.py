import pickle

with open('/Users/benjaminstraate/fletcher/dfs/predictedprocalltweetsnoat.pkl') as pk:
  pred = pickle.load(pk)
  count = 0
  count2 = 0
  for (cat, tweet) in pred:
      count += 1
      if count % 2500 == 0:
          print count, len(pred)
      if cat < 2:
          count2 += 1
          if count2 % 100 == 0:
              print cat
              print tweet
              print 'count2: {}'.format(count2)
              print ''
              print ''
