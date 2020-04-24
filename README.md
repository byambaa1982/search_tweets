---
title: "Get Twitter Data"
date: 2020-04-23 11:33:00 +0800
categories: [Data Mining, Python]
tags: [pandas, lambda, scraping, twitter]
---


## Search Twitter for Tweets

Now you are ready to search Twitter for recent tweets! Start by finding recent tweets that use the `#snowflake` hashtag. You will use the .Cursor method to get an object containing tweets containing the hashtag `#snowflake`.

To create this query, you will define the:

+ Search term - in this case #showflake
+ the start date of your search

Remember that the Twitter API only allows you to access the past few weeks of tweets, so you cannot dig into the history too far.

```python
# Define the search term and the date_since date as variables
search_words = "#snowflake"
date_since = "2020-01-01"
```


Below you use `.Cursor()` to search twitter for tweets containing the search term `#snowflake`. You can restrict the number of tweets returned by specifying a number in the `.items()` method. `.items(5)` will return 5 of the most recent tweets.

```python
# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)
tweets
```
.Cursor() returns an object that you can iterate or loop over to access the data collected. Each item in the iterator has various attributes that you can access to get information about each tweet including:

    1. the text of the tweet
    2. who sent the tweet
    3. the date the tweet was sent

and more. The code below loops through the object and prints the text associated with each tweet.


```python 
# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)

# Iterate and print tweets
for tweet in tweets:
    print(tweet.text)
    
```

The above approach uses a standard for loop. However, this is an excellent place to use a Python list comprehension. A list comprehension provides an efficient way to collect object elements contained within an iterator as a list.


If you have anything to ask, please contact me clicking following link?


You can hire me [here](https://www.fiverr.com/coderjs)

Thank you
