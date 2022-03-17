# Twitter Data Load
# Loads Twitter data into a Pandas Dataframe

# Import Modules
# Standard library imports
import pandas as pd
# Third party imports

# Local imports
import twitter_request_handler as treq
import twitter_print as tprint


# Define Functions

def load_data(search_url, query_params, max_iterations):

    """
    Loads data retrieved from the Twitter API into a Pandas Dataframe
    """


    #------------------------------------
    # Set Up
    # ------------------------------------

    # Create an empty "final" data list
    final_twitter_data_list = []

    # Print the initial query parameters
    tprint.print_start_params (search_url, query_params, max_iterations)

    # Set request iteration counter
    iteration_counter = 1


    # ------------------------------------
    # Initial Request to Twitter API
    # ------------------------------------
    # Make an initial request to check validity of Twitter credentials
    # and the initial query parameters

    # Print the iteration counter for tracking purposes
    tprint.print_iteration(iteration_counter)

    # Print the query parameters used
    tprint.print_iteration_params(query_params)

    # Call Twitter Request function
    twitter_return = treq.twitter_request(search_url, query_params)

    # Now check on the initial Twitter response status code
    initial_status_code = twitter_return['status_code']

    # Print Twitter Response Status Code
    tprint.print_status_code(initial_status_code)

    if initial_status_code != 200:

        # Catch error
        final_status_code = initial_status_code
        message = twitter_return['message']


    # -------------------------------------------
    # Extract Data from Initial Request Response
    # -------------------------------------------
    # If the initial status code = 200, then we are good to go

    if initial_status_code == 200:

        # Keep track of status code
        final_status_code = initial_status_code

        # Grab the Twitter data and meta data
        twitter_data_list = treq.add_data_to_list (twitter_return)
        twitter_meta_dict = treq.extract_meta_data (twitter_return)

        # Print the meta data
        tprint.print_meta_data(twitter_meta_dict)

        # Add the extracted data to the master list using the extend method
        final_twitter_data_list.extend(twitter_data_list)


        # -------------------------------------------
        # Make Additional Requests to Twitter API
        # -------------------------------------------
        # If a 'next_token' key exists in the meta data,
        # there is more data to retrieve for the query

        # Set loop to check for next token key
        while 'next_token' in twitter_meta_dict.keys():


            # Grab more data
            twitter_return = treq.get_more_data(twitter_meta_dict,
                    search_url, query_params)

            # Check on the Twitter response status code
            new_status_code = twitter_return['status_code']


            if new_status_code != 200:

                # Catch error
                final_status_code = new_status_code
                message = twitter_return['message']
                break


            # If the new status code = 200, then we are good to continue

            if new_status_code == 200:

                # Keep track of status code
                final_status_code = new_status_code

                # Check if next iteration will exceed maximum request iterations
                if iteration_counter + 1 > max_iterations:
                    break

                # Update the iteration counter
                iteration_counter = iteration_counter + 1

                # Print the iteration counter for tracking purposes
                tprint.print_iteration(iteration_counter)

                # Print the query parameters used
                tprint.print_iteration_params(query_params)

                # Print Twitter Response Status Code
                tprint.print_status_code(new_status_code)

                # Grab the Twitter data and meta data
                twitter_data_list = treq.add_data_to_list (twitter_return)
                twitter_meta_dict = treq.extract_meta_data (twitter_return)

                # Print the meta data
                tprint.print_meta_data(twitter_meta_dict)

                # Add the extracted data to the master list
                final_twitter_data_list.extend(twitter_data_list)




    # ------------------------------------------------
    # Load All Extracted Data into a Pandas Dataframe
    # ------------------------------------------------

    if final_status_code == 200:

        # Check the keys in the final twitter data list of dictionaries
        # Need to see if an "extra" key named 'withheld' exists
        # for any of the dictionaries
        # And if the key exists, it needs to be deleted
        updated_twitter_data_list=treq.check_final_data_keys(
                final_twitter_data_list)

        # Load the final twitter data into a Pandas dataframe
        df_twitter_data=pd.DataFrame(updated_twitter_data_list)

        # Return the dataframe as output
        output=df_twitter_data


    # -------------------------------------------
    # Prepare Summary of Query Results
    # -------------------------------------------

    if final_status_code == 200:

        # Print Summary Title
        tprint.print_summary_title()

        # Capture total iterations performed
        total_iterations = iteration_counter

        # Print Final Status Code
        tprint.print_final_status_code(final_status_code)

        # Check if the Query managed to complete
        # within the Maximum Request Iterations limit

        if 'next_token' in twitter_meta_dict.keys(): # Query did not complete
            tprint.print_query_incomplete(total_iterations, max_iterations)
        else:
            tprint.print_query_completed(total_iterations, max_iterations)

        # Print the summary contents of resulting dataframe
        tprint.print_dataframe(df_twitter_data)

        # Print End
        tprint.print_end()


    if final_status_code != 200:

        # Print Whoops Error Message
        tprint.print_error_message(final_status_code, message)

    #------------------------------------
    # Wrap Up
    # ------------------------------------

    # Set return
    if final_status_code == 200:
        return output
    else:
        return
