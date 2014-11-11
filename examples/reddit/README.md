This code calculates the similarity between subreddits by the users who comment
in them.  The output of the program should be:

```
[((u'funny', u'pics'), 0.2529296875),
 ((u'funny', u'WTF'), 0.2177734375),
 ((u'funny', u'AskReddit'), 0.2158203125),
 ((u'funny', u'AdviceAnimals'), 0.212890625),
 ((u'WTF', u'pics'), 0.2099609375),
 ((u'AdviceAnimals', u'pics'), 0.205078125),
 ((u'AdviceAnimals', u'WTF'), 0.1884765625),
 ((u'pics', u'AskReddit'), 0.1865234375),
 ((u'AdviceAnimals', u'AskReddit'), 0.169921875),
 ((u'funny', u'gaming'), 0.1669921875),
 ((u'politics', u'worldnews'), 0.1611328125),
 ((u'WTF', u'AskReddit'), 0.16015625),
 ((u'todayilearned', u'worldnews'), 0.1591796875),
 ((u'AdviceAnimals', u'gaming'), 0.15625),
 ((u'videos', u'funny'), 0.1552734375),
 ((u'videos', u'WTF'), 0.1513671875),
 ((u'videos', u'pics'), 0.150390625),
 ((u'WTF', u'gaming'), 0.1494140625),
 ((u'videos', u'todayilearned'), 0.1455078125),
 ((u'todayilearned', u'pics'), 0.14453125),
 ((u'gaming', u'pics'), 0.142578125),
 ((u'videos', u'AdviceAnimals'), 0.1416015625),
 ((u'worldnews', u'news'), 0.1396484375),
 ((u'technology', u'worldnews'), 0.1396484375),
 ((u'videos', u'AskReddit'), 0.134765625)]
```

In order for this code to work, you must have two files, `reddit.json` and
`subreddit_counts.txt.sorted.desc`.  `reddit.json` can be downloaded from
http://www.reddit.com/r/datasets/comments/1mbsa2/155m_reddit_comments_over_15_days/.
The other file, `subreddit_counts.txt.sorted.desc` is a file which contains a
sorted list of all the subreddits by the number of comments seen in the dataset
and is included in this repo.

CHALLENGE: create this file yourself!
