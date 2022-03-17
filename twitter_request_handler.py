# Twitter Request Handler Module
# Module that handles the requests to the Twitter API endpoints.

# Import Modules
# Standard library imports
# Third party imports
# Local imports
import twitter_count_recent_endpoint as ep_count
import twitter_search_recent_endpoint as ep_search
import twitter_print as tprint


# Define Functions

def twitter_request(search_url, query_params):

    """
    Make a request to the Twitter API.
    """
    # Connect to endpoint and get Twitter response (a dictionary)

    if search_url == "https://api.twitter.com/2/tweets/counts/recent":
        twitter_return = ep_count.connect_to_endpoint(search_url, query_params)

    if search_url == "https://api.twitter.com/2/tweets/search/recent":
        twitter_return = ep_search.connect_to_endpoint(search_url, query_params)

    return twitter_return


def add_data_to_list(twitter_return):

    """
    Extract the data from the twitter_return dictionary and place in a list
    """

    twitter_dict = twitter_return ['response_dict']

    # Grab the twitter data
    twitter_data_list=twitter_dict['data']

    return twitter_data_list


def extract_meta_data(twitter_return):

    """
    Extract the meta data from the twitter_return dictionary
    """

    twitter_dict = twitter_return ['response_dict']

    # Grab the returned meta data
    twitter_meta_dict=twitter_dict['meta']

    return twitter_meta_dict


def update_query_params(twitter_meta_dict, query_params):

    """
    Update Query Parameters if next_token key has been returned
    """

    # Grab the next_token key value and assign to a variable
    twitterNextToken=twitter_meta_dict['next_token']

    # Print the value of the next_token
    tprint.print_next_token(twitterNextToken)

    # Add the next_token key/value to the Query Parameters dictionary
    query_params['next_token'] = twitterNextToken

    # Print the updated parameters to be used for the next iteration
    tprint.print_updated_params(query_params)

    return query_params


def get_more_data(twitter_meta_dict, search_url, query_params):

    """
    If next_token key exists, go grab more data from the Twitter API endpoint
    """

    # Update the query parameters with the next_token key
    query_params = update_query_params (twitter_meta_dict, query_params)

    # Call Twitter Request function
    twitter_return = twitter_request(search_url, query_params)

    return twitter_return


def check_final_data_keys(final_twitter_data_list):
    """
    Check for the existence of an "extra" Twitter key
    named 'withheld' in any of the dictionaries.
    And if it exists, then delete it.
    Otherwise it upsets the loading of the data into the dataframe.
    """
    # Optionally print out the keys from the dictionaries in the
    # Final Twitter Data List
    # tprint.print_final_data_keys(final_twitter_data_list)

    # Delete the 'withheld' key and value from the dictionaries
    # in the final twitter data list if they exist

    for row_dict in final_twitter_data_list:

        if 'withheld' in row_dict.keys():
            del row_dict['withheld']

    # Return the updated final twitter data list
    updated_twitter_data_list = final_twitter_data_list

    return updated_twitter_data_list
