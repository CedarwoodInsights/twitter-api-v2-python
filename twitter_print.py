# Twitter Print Module
# Print out tracking information about the requests made to the Twitter API

# Import Modules
# Standard library imports
# Third party imports
# Local imports


# Define Functions

def print_start_params(search_url, query_params, max_iterations):
    """
    Prints the initial query parameters used when
    connecting to Twitter API endpoint
    """
    print (f"\n") # New line
    print ("-" * 40) # Print horizontal line
    print ("INITIAL QUERY PARAMETERS")
    print ("-" * 40) # Print horizontal line

    print(f"\nUsing search_url value: {search_url}")
    print(f"\nUsing query_params value: {query_params}")
    print(f"\nUsing max_iterations value: {max_iterations}")

    return


def print_status_code(code):
    """
    Prints the Twitter Response Status Code
    """
    print(f"\nThe Twitter API Response Code is: {code}")

    return


def print_final_status_code(code):
    """
    Prints the Final Response Status Code
    """
    print(f"\nThe Final Status Code is: {code}")

    return


def print_iteration(iteration_counter):
    """
    Prints the current request iteration number
    """
    # Print a header if it is the first iteration
    if iteration_counter == 1:
        print (f"\n") # New line
        print ("-" * 40) # Print horizontal line
        print(f"BEGIN REQUEST ITERATIONS")
        print ("-" * 40) # Print horizontal line
        print (f"\n") # New line
        print ("-" * 40) # Print horizontal line
        print (f"\nThis is Iteration Number [{iteration_counter}]")

    else:
        # Print the following for all subsequent iterations
        print (f"\n") # New line
        print ("-" * 40) # Print horizontal line
        print (f"\nThis is Iteration Number [{iteration_counter}]")

    return


def print_iteration_params(query_params):
    """
    Prints the query parameters used for the current request iteration
    """
    print(f"\nThe request for this iteration was made with query_params:")
    print (query_params)

    return


def print_meta_data(twitter_meta_dict):
    """
    Print the returned Twitter meta data
    """
    print(f"\nThe twitter_meta_dict value is:")
    print (twitter_meta_dict)

    return


def print_next_token(twitterNextToken):
    """
    Print the value of the Twitter next_token key
    """
    print(f"\nThe twitterNextToken variable value is:")
    print(twitterNextToken)

    return


def print_updated_params(query_params):
    """
    Prints the updated query parameters to be used
    for the next request iteration
    """
    print(f"\nThe updated query_params to be used for the next iteration are:")
    print (query_params)

    return


def print_summary_title():
    """
    Prints the Summary title
    """
    print (f"\n") # New line
    print ("-" * 40) # Print horizontal line
    print (f"SUMMARY")
    print ("-" * 40) # Print horizontal line

    return


def print_error_message(code, message):
    """
    Prints the error message if status code does not equal 200
    """
    print (f"\n") # New line
    print ("-" * 40) # Print horizontal line
    print("WHOOPS")
    print ("-" * 40) # Print horizontal line

    print(f"\nThe Twitter API Response Code is: {code}")
    print(f"\nThe returned message is")
    print(message)

    print ("-" * 40) # Print horizontal line
    print("Program Terminated. Please try again.")
    print ("-" * 40) # Print horizontal line

    return


def print_query_incomplete(total_iterations, max_iterations):
    """
    Prints notification if the query was not completed
    within max iterations limit
    """

    print(f"\nThe total number of request iterations",
            f"performed was {total_iterations}.")
    print(f"\nThe Query results are INCOMPLETE. The Maximum Number",
            f"of Request Iterations has been reached.")
    print(f"\nThe Maximum Number of Request Iterations specified",
            f"was {max_iterations} iterations.")

    return


def print_query_completed(total_iterations, max_iterations):
    """
    Prints notification if the query was successfully completed
    within max iterations limit
    """

    if total_iterations == 1:
        print(f"\nTwitter Query completed after",
                f"{total_iterations} request iteration.")
    else:
        print(f"\nTwitter Query completed after",
                f"{total_iterations} request iterations.")


    print(f"\nThe Maximum Number of Request Iterations specified",
            f"was {max_iterations} iterations.")

    return


def print_final_data_keys(final_twitter_data_list):
    """
    Print the keys from the dictionaries in the Final Twitter Data list
    """

    # Print heading
    print (f"\n") # New line
    print ("-" * 40) # Print horizontal line
    print ("CHECK FINAL TWITTER DATA LIST")
    print ("-" * 40) # Print horizontal line

    # Print the dictionary keys of the first 10 items in the final list.
    print (f"\nThe Keys in the first 10 dictionaries of",
            f"the Final Twitter Data List are:")
    print (f"\n") # New line

    for row_dict in final_twitter_data_list[:10]:

        keys_list=[] # Create an empty list

        for twitter_key in row_dict.keys():
            keys_list.append(twitter_key)

        print (keys_list)

    # Print out all the dictionaries which contain the key 'withheld'
    print ("-" * 40) # Print horizontal line
    print (f"\nThe dictionaries in the Final Twitter Data List",
            f"that contain a 'withheld' key are:")

    print (f"\nSTART List of Dictionaries a 'withheld' key")
    for row_dict in final_twitter_data_list:

        if 'withheld' in row_dict.keys():

            for key, value in row_dict.items():
                print (f"\n Key: {key}")
                print (f"\n Value: {value}")
                print (f"\n") # New line

    print (f"\n...") # Print ellipses
    print (f"\n") # New line
    print (f"END List of Dictionaries with a 'withheld' key")
    print ("-" * 40) # Print horizontal line

    return


def print_dataframe(dataframe):
    """
    Print a summary of the contents of the resulting dataframe
    """

    print (f"\n") # New line
    print ("-" * 40) # Print horizontal line
    # print(f"\nThe dataframe is type: {type(df_twitter_data)}")
    print(f"\nThe dataframe contains the following data:")
    print (f"\n") # New line
    print(dataframe)
    print (f"\n") # New line

    return


def print_end():
    """
    Prints the final End block
    """

    print (f"\n") # New line
    print ("-" * 40) # Print horizontal line
    print (f"\nEND")

    return
