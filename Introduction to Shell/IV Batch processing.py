"""
hell commands will process many files at once. This chapter shows you how to make your own pipelines do that. Along the way, you will
see how the shell uses variables to store information.
"""

## How does the shell store information?
""" ** environment variables === 
         HOME	User's home directory	/home/repl
         PWD	Present working directory	Same as pwd command
         SHELL	Which shell program is being used	/bin/bash
         USER	User's ID	repl
         set   To get a complete list"""
"""Use set and grep with a pipe to display the value of HISTFILESIZE, which determines how many old commands are stored in your command history. What is its value?"""
# set | grep HISTFILESIZE



## How can I print a variable's value?
"""      >>>>>> echo || echo $USER find a variable's value."""
                  
"""The variable OSTYPE holds the name of the kind of operating system you are using. Display its value using echo."""
# $ echo $OSTYPE
# out | linux-gnu



## How else does the shell store information?
"""      ** shell variable == local variable in a programming language.
         >>>>>>   training=seasonal/summer.csv === To create a shell variable (simply assign a value to a name:)          without any spaces """
"""Define a variable called testing with the value seasonal/winter.csv."""
# $ testing=seasonal/winter.csv
"""Use head -n 1 SOMETHING to get the first line from seasonal/winter.csv using the value of the variable testing instead of the name of the file."""
# $ head -n 1 $testing
# out | Date,Tooth



## How can I repeat a command many times?
"""               ** loops
eg.:      for filetype in gif jpg png; do echo $filetype; done
output:  gif
         jpg
         png               
"""
"""Modify the loop so that it prints: docx   ,odt,    pdf"""
# $ for filetype in docx odt pdf; do echo $filetype; done



## How can I repeat a command once for each file?
"""Modify the wildcard expression to people/* so that the loop prints the names of the files in the people directory
regardless of what suffix they do or don't have. Please use filename as the name of your loop variable.
"""
# $ for filename in people/*; do echo $filename; done



## How can I record the names of a set of files?
"""     1| asign a var :  datasets=seasonal/*.csv
        2| display the files' names later:  for filename in $datasets; do echo $filename; done"""
"""---If you run these two commands in your home directory, how many lines of output will they print?
         files=seasonal/*.csv
         for f in $files; do echo $f; done"""
# Four: the names of all four seasonal data files.



## A variable's name versus its value
"""---If you were to run these two commands in your home directory, what output would be printed?
         files=seasonal/*.csv
         for f in files; do echo $f; done."""
# One line: the word "files".
# correct : the loop uses files instead of $files, so the list consists of the word "files".



## How can I run many commands in a single loop?
""" eg:     for file in seasonal/*.csv; do head -n 2 $file | tail -n 1; done
Write a loop that prints the last entry from July 2017 (2017-07) in every seasonal file. It should produce a similar output to:
similar:        grep 2017-07 seasonal/winter.csv | tail -n 1
but for each seasonal file separately. Please use file as the name of the loop variable, and remember to loop through the list of files seasonal/*.csv"""
# $ for file in seasonal/*.csv; do grep 2017-07 $file | tail -n 1; done



## Why shouldn't I use spaces in filenames?
# Both of the above.
# Use single quotes, ', or double quotes, ", around the file names.



#
"""Suppose you forget the semi-colon between the echo and head commands in the previous loop, so that you ask the shell to run:
eg:      for f in seasonal/*.csv; do echo $f head -n 2 $f | tail -n 1; done
---What will the shell do?."""
# Print one line for each of the four files.


