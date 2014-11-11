#!/usr/bin/env python2.7

import ujson as json
from collections import Counter
import os
import sys

if __name__ == "__main__":
    try:
        data_path = sys.argv[1]
    except IndexError:
        data_path = "./"

    reviews = open(os.path.join(data_path, "yelp_academic_dataset_review.json"))
    bid_on_date = []
    for line in reviews:
        if "2010-04-25" in line:
            data = json.loads(line)
            bid_on_date.append(data['business_id'])
            
    cities = Counter()
    businesses = open(os.path.join(data_path, "yelp_academic_dataset_business.json"))
    for business in businesses:
       data = json.loads(business)
       if data['business_id'] in bid_on_date:
           cities[data['city']] += 1

    print cities
"""
Counter({u'Las Vegas': 116, u'Phoenix': 55, u'Tempe': 18, u'Henderson': 13, u'Edinburgh': 11, u'Scottsdale': 10, u'Glendale': 9, u'Madison': 8, u'Gilbert': 6, u'Mesa': 6, u'Chandler': 5, u'Waterloo': 5, u'Queen Creek': 2, u'Cave Creek': 2, u'Sun City': 1, u'Anthem': 1, u'Maricopa': 1, u'Middleton': 1, u'Kitchener': 1})
"""
