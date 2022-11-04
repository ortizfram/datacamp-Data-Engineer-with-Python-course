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
