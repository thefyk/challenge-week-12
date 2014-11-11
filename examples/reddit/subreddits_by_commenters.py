import ujson as json
import csv
from itertools import islice
from countmemaybe import KMinValues
from collections import (defaultdict, Counter)

if __name__ == "__main__":
    reddit = open("reddit.json")
    subreddits = defaultdict(lambda : KMinValues(k=1024))

    subreddit_counts = islice(csv.reader(open("subreddit_counts.txt.sorted.desc"), delimiter=' '), 50)
    top_50 = set(item[-1] for item in subreddit_counts)
    for item in reddit:
        data = json.loads(item)
        if data['subreddit'] in top_50:
            subreddits[data['subreddit']].add(data['author'])
       
    subreddits_list = subreddits.items()
    similarity = Counter()
    for i, (k1, v1) in enumerate(subreddits_list[:-1]):
        for j, (k2, v2) in enumerate(subreddits_list[i+1:], i+1):
            similarity[(k1, k2)] = v1.jaccard(v2)
    print similarity.most_common(25)

