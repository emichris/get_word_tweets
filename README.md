# Python Script to Download Tweets

### Introduction
**Gathering Tweet Data using Twitter API and Tweety Python Library**<br>
Information about the Tweety Python Library can be found at [docs.tweepy.org](http://docs.tweepy.org/en/v3.1.0/api.html#API.search). Information about Twitter's `Standard Search API` can be found [here](https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets)

### Setup
In order to use the script, you need to get your Twitter API Credentials by creating a new app at [developer.twitter.com](developer.twitter.com). The script uses Tweepy Python Library, you can install the library by running th following command in the terminal first:

```
$ pip install tweepy
```

### Clone and use the Python script
Now you're ready to clone and use the get_tweets script.

```
$ git clone https://github.com/emichris/get_word_tweets.git
$ cd get_tweets
```
Enter the appropriate keys from your Twitter developer account in lines 7-11 of `get_word_tweets.py` using any text editor.

Finally you can run the script by entering the word you will like to query and if you like how many reults you will like to return. Please note, there is a limit set by Twitter on the number of twitter data you can download. 

```
$ python get_word_tweets.py StayAtHome 500
```
This will store 500 tweets using Twitter in th file StayAtHome_tweets.csv

```
$ python get_word_tweets.py StayAtHome
```
without the second argument, the default number of results is 100 tweets