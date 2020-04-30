import sys
import csv
import tweepy
import pandas as pd

#Get your Twitter API credentials and enter them here
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_key = "your_access_key"
access_secret = "your_access_secret"

#http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# authenticate the api with token and access information
api = tweepy.API(auth, wait_on_rate_limit=True)


def get_word_tweets(query='Happy', num_result = 100):
    '''
    input: 
        api - twitter api
        query - words to use for query 
        num_result 
    ouput: 
        a transformed data frame object
    '''
     
    json_data = []; n = 0;
    while n < num_result: 
        for search_result in api.search(query, lang='en', count=num_result-n):
            if n > num_result: 
                break 
            n = n + 1
            json_data.append(search_result._json)
    
    df = pd.io.json.json_normalize(json_data)
    
    # To check all available columns in the created dataframe use print(list(df.columns))
    
    df = df[['id', 'created_at', 'text', 'favorite_count', 'retweet_count', 'truncated']] #select desired columns
    
    
    df.to_csv(query+'_tweets.csv', index=False, encoding=False) # write to csv file
    print("Done. Your csv file is saved to "+query+'_tweets.csv')
              
#if we're running this as a script
if __name__ == '__main__':

    #get tweets for username passed at command line
    if len(sys.argv) == 2:
        get_word_tweets(sys.argv[1])
    else: 
        if len(sys.argv) == 3:
            get_word_tweets(sys.argv[1], int(sys.argv[2]))
        else:
            print ("Error: enter a valid query")
