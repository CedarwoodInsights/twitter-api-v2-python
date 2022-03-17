# Twitter Search Recent Endpoint Module
# Connect to the Twitter API Tweet Search Recent endpoint

# Import Modules
# Standard library imports
import requests
import os
import json

# Third party imports

# Local imports
import twitter_bearer_token as bt

# Load Twitter Credentials
# Set the required Environment Variable
bt.set_environment_variable()


# Set the bearer_token variable by grabbing the value
# from the Environment Variables.
bearer_token = os.environ.get("BEARER_TOKEN")
# print(os.environ["BEARER_TOKEN"])

# Define Functions

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython" # Parameterise?
    return r


def connect_to_endpoint(url, params):
    """
    Make request to Twitter API endpoint
    """

    response = requests.get(url, auth=bearer_oauth, params=params)


    # Check the Twitter API response status code
    if response.status_code == 200:

        response_dict = response.json() # Python dictionary
        code = response.status_code

        # Return a dictionary
        twitter_return = {'status_code':code, 'response_dict': response_dict}

    if response.status_code != 200:
        code = response.status_code
        text = response.text

        # Debug
        # print (f"\nERROR DETECTED")
        # print (f"\nThe Twitter Response Status Code is: {code}")
        # print (f"\nThe Twitter Response Text is:")
        # print (f"\n{text}")

        # Call function to go grab the error message
        message=status_code_check(code, text)

        # Return a dictionary
        twitter_return = {'status_code': code, 'message': message}

    return twitter_return


def status_code_check(code, text):
    """
    Check details of Twitter API Response Codes
    """

    # The response from the Twitter API is in JSON form
    text_json = text
    # print (f"\nThe response is type: {type(text_json)}")

    # Load JSON response into a Python dictionary
    text_dict = json.loads(text_json)
    # print (f"\nThe text_dict is: {type(text_dict)}")
    # print (f"\nThe contents of text_dict are:")
    # print (text_dict)

    # Grab Errors list from the Text dictionary
    errors_list = text_dict['errors']
    # print (f"\nThe errors_list is: {type(errors_list)}")
    # print (f"\nThe contents of errors_list are:")
    # print (errors_list)

    # Create Errors dictionary from Errors List
    errors_dict = errors_list[0]
    # print (f"\nThe errors_dict is: {type(errors_dict)}")
    # print (f"\nThe contents of errors_dict are:")
    # print (errors_dict)

    # Grab Message from Errors dictionary
    message = errors_dict['message']
    # print (f"\nThe message is: {type(message)}")
    # print (f"\nThe contents of message are:")
    # print (message)

    return message
