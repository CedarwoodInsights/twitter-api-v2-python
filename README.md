# Twitter API v2 Python
Jupyter Notebook and Python code to query Twitter data using the Twitter API v2.

## What does the code do?
Submit "simple" queries to the following Twitter API v2 endpoints:
- Tweets Counts Recent - See: [Tweet Counts API Reference](https://developer.twitter.com/en/docs/twitter-api/tweets/counts/api-reference/get-tweets-counts-recent)
- Tweets Search Recent - See: [Search Tweets API Reference](https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent)

The query results are returned in a Pandas Dataframe.

## Prerequisites
You need to apply for a Twitter Developer account with "Elevated" access.

See: [How to get access to the Twitter API](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api)

With elevated access you will be allowed to query "recent" Twitter data for
the last 7 days.

## Twitter API v2 Sample Code
The underlying Python code used for accessing the Twitter endpoints is sourced
from twitterdev on GitHub here:

[Twitter-API-v2-sample-code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

In particular:

[Recent Tweet Counts Python code](https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Recent-Tweet-Counts/recent_tweet_counts.py)

[Recent Search Python code](https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Recent-Search/recent_search.py)


## Jupyter Notebooks
Two Jupyter Notebooks are provided:
- twitter_count_recent_main.ipynb
- twitter_search_recent_main.ipynb

These can be run directly from Jupyter. Alternatively the main() function
within each notebook may be called from an external application.


## Stuff to mention
- Log files - need to manualy create a folder (eg log_files)
- Error handling
- KNIME?
- Bearer Token - need to paste into the twitter bearer token module.
- Code is based on Twitter Dev Python code
