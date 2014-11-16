# Challenge Week 12 Submission Template

# Reddit Data Challenges

## Challenge 1

![Screenshot](http://i.imgur.com/BcyoaFv.png)

## Challenge 2

The subreddits that get the most comments overall are highly related to the subreddits that appear on the front page. It's interesting too see such informal ranting structured in JSON format.

## Challenge 3

Sentiment analysis could be done on this data to find which subreddits have the most positive comments and who the most positive commenters are, and how that relates to one's comment score (along with analyzing key words). This data set could provide insight on the relation between comment success and comment frequency).

## Challenge 4

It could tell you the topics that interest the Reddit community the most (through analyzing subreddits and keywords) and could tell you which topics were more likely to spur reactions from reddit users.

## Challenge 5

[Link to Code or pasted code]
[Answer]

## Challenge 6

The results would be different because the analysis would likely skew to promote subreddits that were either more popular or more likeminded (as their viewers would often be upvoting the same people).

## Challenge 7

The conclusions of the results would change, but my conclusion would not as I would account for the fact that the query would be answering a different question.

## Challenge 8

Subreddits with very small amounts of comments can have very high Jaccard's distances because the distance is a proportion. So even if two sets are 100% similar, it could just be because the same person created two subreddits and commented once in each which is not very representative of the question.

## Challenge 9

The time period in which the data was collected, potential interference in storing/retreiving the data, and the fact that the Reddit API only serves http 500s. Considering that there is no question being asked regarding the whole data set, the biases are limited.

## Challenge 10

I could prove the bias by collecting data over a different time period and comparing the results. If the results were different, I could look at a much larger data set and see how much different the results were over that time period as well.

# Yelp and Weather 

## Challenge 1

![Screenshot](http://i.imgur.com/7r9CCnF.png)

[Query: db.precip.aggregate([{$match: {"STATION_NAME":"MADISON DANE CO REGIONAL AIRPORT WI US", "DATE":/^20100425/}}, {$group: {_id: "$STATION_NAME", total:{$sum:"$HPCP"}}}])]

[Result: 62]

## Challenge 2

2.Query: db.normal.aggregate([{$match: {"STATION_NAME":"LAS VEGAS MCCARRAN INTERNATIONAL AIRPORT NV US", "DATE":/^20100425/}}, {$group: {_id: "$STATION_NAME", average:{$avg:"$HLY-WIND-AVGSPD"}}}])

Result: 110.0833

## Challenge 3

3. > db.yelpbus.aggregate([{$match: {"city":"Madison"}}, {$group: {_id: "$city", total: {$sum:"$review_count"}}}])

{ "_id" : "Madison", "total" : 34410 }

## Challenge 4

4. > db.yelpbus.aggregate([{$match: {"city":"Las Vegas"}}, {$group: {_id: "$city", total: {$sum:"$review_count"}}}])

{ "_id" : "Las Vegas", "total" : 577550 }

## Challenge 5

> db.yelpbus.aggregate([{$match: {"city":"Phoenix"}}, {$group: {_id: "$city", total: {$sum:"$review_count"}}}])

{ "_id" : "Phoenix", "total" : 200089 }





