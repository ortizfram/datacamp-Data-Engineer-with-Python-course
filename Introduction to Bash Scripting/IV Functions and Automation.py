"""
you will learn the structure of functions in Bash, how to use functions to help automate frequent tasks, and program your scripts torun on schedule without
needing to even lift a finger.
"""
"""
*** Functions:
    - reusable  - modular code
    *** Bash function Syntax:
        eg:
            function_name () {
                # funtion code
                return # something
            }
        eg:    
            # call it using only name
            function_name2 () {
                echo "hello vato"
            }
            
            # the call
            function_name2
            -hello vato
"""

"""
### Uploading model results to the cloud

Instructions

- Set up a function using the 'function-word' method called upload_to_cloud.
- Use a FOR statement to loop through (using glob expansion) files whose names contain results in output_dir/ and echo that the filename is being uploaded to the cloud.
- Call the function just below the function definition using its name.

For technical reasons, no files will be uploaded; we will simply echo out the file name. Though you could easily replace 
this section with code to upload to Amazon S3, Google Cloud or Microsoft Azure!
"""
# Create function
function upload_to_cloud () {
  # Loop through files with glob expansion
  for file in output_dir/*results*
  do
    # Echo that they are being uploaded
    # section could be replaced to: upload Amazon S3, Google Cloud or Microsoft Azure!
    echo "Uploading $file to cloud"
  done
}

# Call the function
upload_to_cloud

"""
### Get the current day

Instructions

You want to extract the Fri part only.
- Set up a function called what_day_is_it without using the word function (as you did using the function-word method).
- Parse the output of date into a variable called current_day. The extraction component has been done for you.
- Echo the result.
- Call the function just below the function definition.
"""
# Create function
what_day_is_it () {

  # Parse the results of date
  current_date=$(date | cut -d " " -f1)

  # Echo the result
  echo $current_date
}

# Call the function
what_day_is_it


repl:~/workspace$ bash script.sh
Fri

"""
*** Scope in programmming
    >>>>>> 'Global' : accessible anywhere in the program
    >>>>>> 'Local' : accessible only in ceratain part of the program; like inside a for 
    
    *** All vars in Bash are GLOBALly BY default   
"""

"""
### A percentage calculator

Instructions

- Create a function called return_percentage using the function-word method.
- Create a variable inside the function called percent that divides the first argument fed into the function by the second argument.
- Return the calculated value by echoing it back.
- Call the function with the mentioned test values of 456 (the first argument) and 632 (the second argument) and echo the result.
"""
# Create a function 
function return_percentage () {

  # Calculate the percentage using bc
  percent=$(echo "scale=2; 100 * $1 / $2" | bc)

  # Return the calculated percentage
  echo $percent
}

# Call the function with 456 and 632 and echo the result
return_test=$(return_percentage 456 632)
echo "456 out of 632 as a percent is $return_test%"


repl:~/workspace$ bash script.sh
456 out of 632 as a percent is 72.15%

"""
### Sports analytics function

- Create a function called get_number_wins using the function-word method.
- Create a variable inside the function called win_stats that takes the argument fed into the function to filter the last step of the shell-pipeline presented.
- Call the function using the city Etar.
- Below the function call, try to access the win_stats variable created inside the function in the echo command presented.
"""
# Create a function
function get_number_wins () {

  # Filter aggregate results by argument
  win_stats=$(cat soccer_scores.csv | cut -d "," -f2 | egrep -v 'Winner'| sort | uniq -c | egrep "$1")

}

# Call the function with specified argument
get_number_wins "Etar"

# Print out the global variable
echo "The aggregated stats are: $win_stats"

"""
### Create a function with a local base variable

An array of numbers you can use for a test of your function would be the daily sales in your organization this week (in thousands):

14 12 23.5 16 19.34 which should sum to 84.84

Instructions

- Create a function called sum_array and add a base variable (equal to 0) called sum with local scope. You will loop through the array and increment this variable.
- Create a FOR loop through the ARGV array inside sum_array (hint: This is not $1! but another special array property) and increment sum with each element of the array.
- Rather than assign to a global variable, echo back the result of your FOR loop summation.
- Call your function using the test array provided and echo the result. You can capture the results of the function call using the shell-within-a-shell notation.
"""
# Create a function with a local base variable
function sum_array () {
  local sum=0
  # Loop through, adding to base variable
  for number in "$@"
  do
    sum=$(echo "$sum + $number" | bc)
  done
  # Echo back the result
  echo $sum
  }
# Call function with array
test_array=(14 12 23.5 16 19.34)
total=$(sum_array "${test_array[@]}")
echo "The total sum of the test array is $total"


repl:~/workspace$ bash script.sh
The total sum of the test array is 84.84

"""
*** Scheduling your scripts with Cron
    -WHY ?
        regular tasks need to be done daily.
        optimal use of resources.
    -CRON ?
        driven by smt called 'crontab'.
            this file contains 'cronjobs' that tells what to run and when.
            
    crontab -l >>>>>> see current cronjobs
    
     *** How to time a cron job : 
              * minute (0-59)
              ** hour (0-23)
              *** day of month  (1-31)
              **** month  (1-12)
              ***** day of week (0-6) (0 is Sunday)
              
        *** first 'cronjob'
            >>>>>> crontab -i : edit crontab w/ nano
"""

"""
### Analyzing a crontab schedule

- Can you determine how often the script.sh Bash script will run if the following line is in the user's crontab?
    15 * * * 6,7 bash script.sh
    
Answer : 15 minutes past every hour on Saturdays and Sundays.
"""

"""
### Creating cronjobs
"""
# Create a schedule for 30 minutes past 2am every day
30 2 * * * bash script1.sh

# Create a schedule for every 15, 30 and 45 minutes past the hour
15,30,45 * * * bash script2.sh

# Create a schedule for 11.30pm on Sunday evening, every week
30 23 * * 0 bash script3.sh

"""
### Scheduling cronjobs with crontab

Instructions 1/3

1
Verify there are no existing cronjobs by listing them.
2
Use the edit command for crontab (select nano) then schedule extract_data.sh to run with Bash at 2:30am every day.
3
Verify the cronjob has been scheduled in the crontab by listing all current scheduled cronjobs.
"""
repl:~$ crontab -l
    # This is your crontab file.
    # Schedule your crontabs below.
repl:~$ nano crontab
    30 2 * * * extract_data.sh
    # (save,exit) contrl O + contrl X
repl:~$ crontab -l
