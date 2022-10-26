""" brief introduction to the Unix shell. You'll learn why it is still in use after almost 50 years, how it compares to the graphical tools
you may be more familiar with, how to move around in the shell, and how to create, modify, and delete files and folders.
"""


## How does the shell compare to a desktop interface?
"""---What is the relationship between the graphical file explorer that most people use and the command-line shell?"""
# They are both interfaces for issuing commands to the operating system.


## Where am I?
  """ >>>>>> $ pwd === print working directory."""
# /home/repl


## How can I identify files and directories?
  """ >>>>>> $ cd === go inside directory."""
  """ >>>>>> $ ls ===  list the files in the directory."""

"""---Which of these files is not in that directory?."""
# $ cd seasonal
# $ ls         
# fall.csv


## How else can I identify files and directories?
""" **PATH : If it begins with /, it is absolute. If it does not begin with /, it is relative."""
# ls course.txt
# $ ls seasonal/summer.csv


## How can I move to another directory?
# cd seasonal
# pwd
# ls


## How can I move up a directory?
"""---If you are in /home/repl/seasonal, where does cd ~/../. take you?"""
# /home


## How can I copy files?
"""  >>>>>> cp original.txt duplicate.txt === creates a copy and renames."""
"""copy summer.csv in seasonal, to backup file, as summer.bck"""
# cp original.txt duplicate.txt

"""Copy spring.csv and summer.csv from the seasonal directory into the backup directory without changing your current working directory (/home/repl)."""
# cp seasonal/spring.csv seasonal/summer.csv backup


## How can I move a file?
"""   >>>>>> mv === move a file,rename a file. same syntax as cp."""
"""You are in /home/repl, which has sub-directories seasonal and backup. Using a single command, move spring.csv and summer.csv from seasonal to backup."""
# mv seasonal/spring.csv seasonal/summer.csv backup


## How can I rename files?
"""Rename the file winter.csv to be winter.csv.bck."""
# $ cd seasonal
# $ ls
# autumn.csv  spring.csv  summer.csv  winter.csv
# $ mv winter.csv winter.csv.bck
# $ ls
# autumn.csv  spring.csv  summer.csv  winter.csv.bck


## How can I delete files?
"""   >>>>>> rm === remove file through terminal."""
"""Remove autumn.csv from seasonal, then go back and remove autumn.csv from seasonal."""
# $ cd seasonal
# $ rm autumn.csv
# $ cd ..
# $ rm seasonal/summer.csv


## How can I create and delete directories?
"""Without changing directories, delete the file agarwal.txt in the people directory."""
# rm -r people/agarwal.txt
"""Now that the people directory is empty, use a single command to delete it."""
# rmdir people
"""   >>>>>> rmdir === remove empty folder."""
"""   >>>>>> mkdir === create a directory."""
"""create a directory/folder"""
# mkdir yearly
"""early exists, create another directory called 2017 inside it without leaving your home directory."""
# $ mkdir yearly/2017


## Wrapping up
""" ** create intermediate files when analyzing data. Rather than storing them in your home directory, you can put them in /tmp,/tmp is 
    ** immediately below the root directory /  """
"""   >>>>>> /tmp ===temp folder"""
"""   >>>>>> ~ ===shortcut for '/home/repl' """
"""|| Move /home/repl/people/agarwal.txt into /tmp/scratch"""
# $ cd /tmp
# $ ls
# $ mkdir scratch
# $ mv ~/people/agarwal.txt /tmp/scratch
