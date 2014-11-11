#!/usr/bin/env python2.7

import ujson as json
import csv
from itertools import islice
from collections import (defaultdict, Counter)
from countmemaybe import KMinValues
import sys
import os

if __name__ == "__main__":
    try:
        data_path = sys.argv[1]
    except IndexError:
        data_path = "./"

    reddit = open(os.path.join(data_path, "reddit.json"))
    subreddits = defaultdict(lambda : KMinValues(k=1024))

    subreddit_counts = csv.reader(open(os.path.join(data_path, "subreddit_counts.txt.sorted.desc")), delimiter=' ')
    top_50 = set(item[-1] for item in islice(subreddit_counts, 50))
    print "Finding commenters"
    for item in reddit:
        data = json.loads(item)
        if data['subreddit'] in top_50:
            subreddits[data['subreddit']].add(data['author'])
       
    subreddits_list = subreddits.items()
    similarity = Counter()
    print "Calculating similarity"
    for i, (k1, v1) in enumerate(subreddits_list[:-1]):
        for j, (k2, v2) in enumerate(subreddits_list[i+1:], i+1):
            similarity[(k1, k2)] = v1.jaccard(v2)
    print similarity.most_common(25)

