---
title: "Get Twitter Data"
date: 2020-04-23 11:33:00 +0800
categories: [Data Mining, Python]
tags: [pandas, lambda, scraping, twitter]
---


##Search Twitter for Tweets

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