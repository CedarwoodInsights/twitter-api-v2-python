# Twitter API v2 Python
Jupyter Notebook and Python code to query Twitter data using the Twitter API v2.

## Overview
Submit "simple" queries to the following Twitter API v2 endpoints:
- Tweets Counts Recent - See: [Tweet Counts API Reference](https://developer.twitter.com/en/docs/twitter-api/tweets/counts/api-reference/get-tweets-counts-recent)
- Tweets Search Recent - See: [Search Tweets API Reference](https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent)

The query results are returned in a Pandas Dataframe. Hence the assumption of "simple" queries that will return non-nested "tabular" results.

The code handles making iterative API requests in response to receipt of Twitter "next_token" keys. Some limited HTTP Request error handling is also built in to allow the code to fail silently if the HTTP status code does not equal 200. Finally, a log file is automatically generated to allow tracking of the API request iterations for audit purposes.

## Prerequisites
You need to apply for a Twitter Developer account with "Elevated" access.

See: [How to get access to the Twitter API](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api)

With elevated access you will be allowed to query "recent" Twitter data for
the last 7 days.

Then using your (new) Twitter Developer account you need to generate a Twitter API "Bearer Token" for authentication.

See: [Twitter Authentication](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens)

Once you have your Twitter Bearer Token, copy and paste this into the attached "twitter_bearer_token.py" file as follows:

        def set_environment_variable():
              os.environ["BEARER_TOKEN"]="<Paste your Twitter Bearer Token here, inside the quotation marks.>"
              return

## Twitter API v2 Sample Code
The underlying Python code used for accessing the Twitter endpoints is sourced
from twitterdev on GitHub here:

[Twitter-API-v2-sample-code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

In particular:

[Recent Tweet Counts Python code](https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Recent-Tweet-Counts/recent_tweet_counts.py)

[Recent Search Python code](https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Recent-Search/recent_search.py)

The source Twitter API v2 Sample code is used under the this [license.](https://github.com/twitterdev/Twitter-API-v2-sample-code#license) Note that the Twitter sample source code has been modified for use here.



## Jupyter Notebooks
Two Jupyter Notebooks are provided as the main entry points to run the code:
- twitter_count_recent_main.ipynb
- twitter_search_recent_main.ipynb

These can be run directly from Jupyter. Alternatively the main() function
within each notebook may be called from an external application.

## Log Files



## License
Copyright 2022 Cedarwood Insights Limited.

Licensed under the Apache License, Version 2.0: https://www.apache.org/licenses/LICENSE-2.0


## Stuff to mention
- Log files - need to manualy create a folder (eg log_files)
- Error handling
- KNIME?
-
