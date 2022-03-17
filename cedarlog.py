# Cedarwood Log File Generator
# Module used to generate a log file and
# to divert the standard output accordingly.

# Import Modules
# Standard library imports
import sys
from datetime import datetime

# Third party imports
# Local imports


# Define Functions

def use_log_file (switch, log_file_name='',
        stdout_fileno='', title='', location=''):
    """
    Open and close a log file, and redirect standard output accordingly
    """

    # Grab log files folder location
    log_file_location = location

    if switch == "open":
        # datetime object containing current date and time
        now = datetime.now()
        # print("now =", now)

        # Convert date time to a string (in desired format)
        date_time_string = now.strftime("%y%m%d_%H%M%S_")
        # print(f"Date and Time String is: {date_time_string}")

        # Generate Log File Name
        log_file_name = f"{date_time_string}{title}.txt"
        # print(log_file_name)

        # Save the current stdout so that we can revert back later
        stdout_fileno = sys.stdout

        # Redirect print output (stdout) to the log file
        sys.stdout = open(f"{log_file_location}/{log_file_name}", 'a')

        print (f"\nLog file name is: {log_file_name}")
        print (f"\nLog file location is: {log_file_location}")



    if switch == "close":
        # Close the log file (redirect standard output back to default)
        sys.stdout.close()

        # Restore the original stdout
        sys.stdout = stdout_fileno

        # Read the generated log file (as standard output)
        with open(f'{log_file_location}/{log_file_name}') as file_object:
            log_file_contents = file_object.read()
        print (f"\n") # New line
        print (log_file_contents)



    return (log_file_name, stdout_fileno, log_file_location) # Return a tuple
