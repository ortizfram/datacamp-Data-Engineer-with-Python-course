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
        
        *** shell prectice :
            - run : grep 'p' fruits.txt
              apple
            - run : grep '[pc]' fruits.txt
              apple, carrot
            - run : sort | uniq -c  ----to count
      
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
