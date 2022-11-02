"""~~~
Save yourself time when performing complex repetitive tasks. You’ll begin this course by refreshing your knowledge of common command-line programs and arguments
before quickly moving into the world of Bash scripting. You’ll create simple command-line pipelines and then transform these into Bash scripts. You’ll then boost 
your skills and learn about standard streams and feeding arguments to your Bash scripts.
"""

"""
*** Shel command refreshers :
        (e)grep : filter input based on regex pattern matching
        cat : concatenates file contents line-by-line
        tail/head : gives only the last -n (flag) lines
        wc : word or line count (flags -w -l)
        sed : pattern matched string replacement 
        
        *** shell practice :
            - run : grep 'p' fruits.txt
              apple
            - run : grep '[pc]' fruits.txt
              apple, carrot
            - run : sort | uniq -c  ----to count
            
            *** Word separation shell syntax : 
                 eg : repl:~$ cat two_cities.txt | egrep 'Sydney Carton|Charles Darnay'
      
** REGEX : regular expressions, vital skill for bash script

"""

"""
### Extracting scores with shell

There is a file in either the start_dir/first_dir, start_dir/second_dir or start_dir/third_dir directory called soccer_scores.csv. 
  It has columns Year,Winner,Winner Goals for outcomes of a soccer league.
  
-cd into the correct directory and use cat and grep to find who was the winner in 1959. You could also just ls from the top directory if you like!

terminal:   repl:~$ cd start_dir/second_dir/
            repl:~/start_dir/second_dir$ cat soccer_scores.csv | grep 1959
            1959,Dunav,2
            
Answer : Dunav

"""

"""
### Searching a book with shell

There is a copy of Charles Dickens's infamous 'Tale of Two Cities' in your home directory called two_cities.txt.

-Use command line arguments such as cat, grep and wc with the right flag to count the number of lines in the book that contain either the
 character 'Sydney Carton' or 'Charles Darnay'. Use exactly these spellings and capitalizations.
 
Terminal : repl:~$ cat two_cities.txt | egrep 'Sydney Carton|Charles Darnay' | wc -l

Answer : 77

"""

"""
Your first Bash script

>>>>>> which bash  : o check lcoation of bash you're runing
>>>>>> bash script_name.sh  or  ./script_name.sh: run bash script

*** bash Anatomy : .sh

"""

"""
### A simple Bash script

For this environment bash is not located at /usr/bash but at /bin/bash. You can confirm this with the command which bash.

There is a file in your working directory called server_log_with_todays_date.txt. 
-Your task is to write a simple Bash script that concatenates this out to the terminal so you can see what is inside
-Create a single-line script that concatenates the mentioned file.
-Save your script and run from the console.
        
        
Pane of script.sh :     #!/bin/bash

                        # Concatenate the file
                        cat server_log_with_todays_date.txt


                        # Now save and run!
"""
