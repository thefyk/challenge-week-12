import string
import ujson as json
from collections import Counter

def extract_ngrams(words, N=2):
    for i in xrange(len(words)-N+1):
        yield tuple(words[i:i+N])
        
def extract_words(text):
    words = text.split(" ")
    for word in words:
        word = word.strip(string.punctuation).lower()
        if word:
            yield word

if __name__ == "__main__":
    ngrams = Counter()
    reviews = open("yelp_academic_dataset_review.json")
    for line in reviews:
        if "2010-04-25" in line:
            data = json.loads(line)
            ngrams.update(extract_ngrams(list(extract_words(data['text']))))
    ngrams.most_common(5)

"""
[((u'of', u'the'), 177),
 ((u'in', u'the'), 129),
 ((u'and', u'the'), 122),
 ((u'this', u'place'), 121),
 ((u'it', u'was'), 112)]
"""
