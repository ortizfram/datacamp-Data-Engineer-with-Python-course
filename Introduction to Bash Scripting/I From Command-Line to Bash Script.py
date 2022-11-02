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
        
        
Pane :  #!/bin/bash

        # Concatenate the file
        cat server_log_with_todays_date.txt


        # Now save and run!
"""

"""
### Shell pipelines to Bash scripts

Your job is to create a Bash script from a shell piped command which will aggregate to see how many times each team has won.

-Create a single-line pipe to cat the file, cut out the relevant field and aggregate (sort & uniq -c will help!) based on winning team.
-Save your script and run from the console.

Pane:   #!/bin/bash

        # Create a single-line pipe
        cat soccer_scores.csv | cut -d "," -f 2 | tail -n +2 | sort | uniq -c

        # Now save and run!
out: 13 Arda
      8 Beroe
      9 Botev
      8 Cherno
     17 Dunav
     15 Etar
      4 Levski
      1 Lokomotiv
"""

"""
### Extract and edit using Bash scripts

-You will need to create a Bash script that makes use of sed to change the required team names.

-Create a pipe using sed twice to change the team Cherno to Cherno City first, and then Arda to Arda United.
-Pipe the output to a file called soccer_scores_edited.csv.
-Save your script and run from the console. Try opening soccer_scores_edited.csv using shell commands to confirm it worked (the first line should be changed)!

Pane :  #!/bin/bash

        # Create a sed pipe to a new file
        cat soccer_scores.csv | sed 's/Cherno/Cherno City/g' | sed 's/Arda/Arda United/g' > soccer_scores_edited.csv

        # Now save and run!

"""

"""
Standard streams & arguments

*** arguments : 
               >>>>>> $   $1   $2 : to access bash arguments
                 >>>>>>  $@  or @*  : access all arguments
                 >>>>>>  $# : give length of arguments 
"""

### Using arguments in Bash scripts

# Echo the first and second ARGV arguments
echo $1 
echo $2

# Echo out the entire ARGV array
echo $@

# Echo out the size of ARGV
echo $#


repl:~/workspace$ bash script.sh Bird Fish Rabbit
        
"""
### # Echo the first ARGV argument

-Echo the first ARGV argument so you can confirm it is being read in.
-cat all the files in the directory /hire_data and pipe to grep to filter using the city name (your first ARGV argument).
-On the same line, pipe out the filtered data to a new CSV called cityname.csv where cityname is taken from the first ARGV argument.
-Save your script and run from the console twice (do not use the ./script.sh method). Once with the argument Seoul. Then once with the argument Tallinn.
"""
# Echo the first ARGV argument
echo $1 

# Cat all the files
# Then pipe to grep using the first ARGV argument
# Then write out to a named csv using the first ARGV argument
cat hire_data/* | grep "$1" > "$1".csv


repl:~/workspace$ bash script.sh Seoul
Seoul
repl:~/workspace$ bash script.sh Tallinn
Tallinn 
