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

