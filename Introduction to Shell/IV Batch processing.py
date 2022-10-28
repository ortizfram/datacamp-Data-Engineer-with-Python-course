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
