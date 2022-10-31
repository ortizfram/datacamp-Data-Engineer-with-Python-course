"""
History lets you repeat things with just a few keystrokes, and pipes let you combine existing commands to create new ones. In this chapter,
you will see how to go one step further and create new commands of your own.
"""

## How can I edit a file?
"""text editor Nano. If you type 
      >>>>>> nano filename === it will open/create/edit filename for editing
          ** operations with control-key combinations:
              Ctrl + K: delete a line.
              Ctrl + U: un-delete a line.
              Ctrl + O: save the file ('O' stands for 'output'). You will also need to press Enter to confirm the filename!
              Ctrl + X: exit the editor."""
"""---Run nano names.txt to edit a new file in your home directory and enter the following four lines:"""
# $ nano names.txt
# paste| Lovelace
#        Hopper
#        Johnson
#        Wilson
# cntrl + O : save  then press ENTER
# cntrl + X : leave file



## How can I record what I just did?
"""Copy the files seasonal/spring.csv and seasonal/summer.csv to your home directory."""
""" >>>>>> cp === copy."""
# $ cp seasonal/s* ~
"""Use grep with the -h flag (to stop it from printing filenames) and -v Tooth (to select lines that don't match the header line) 
to select the data records from spring.csv and summer.csv in that order and redirect the output to temp.csv."""
""" >>>>>> grep -h === dont print filenames.
    >>>>>> > temp.csv === redirect ooutput to temp.csv."""
# $ grep -h -v Tooth seasonal/s* > temp.csv
"""Pipe history into tail -n 3 and redirect the output to steps.txt to save the last three commands in a file.
(You need to save three instead of just two because the history command itself will be in the list.)"""
""" >>>>>> history tail -3 === give last 2 steps in hestory"""
# $ history tail -n 3 > steps.txt



## How can I save commands to re-run later?
"""Use nano dates.sh to create a file called dates.sh that contains this command:
            cut -d , -f 1 seasonal/*.csv
to extract the first column from all of the CSV files in seasonal."""
""" >>>>>>> nano filename.sh === create saved command in bash program
    >>>>>>> bash filename.sh === run saved bash programm"""
# $ nano dates.sh
# cut -d , -f 1 seasonal/*.csv
# (save and exit)
# $ bash dates.sh



## How can I re-use pipes?
""" ** file full of shell commands is called a *shell script, or sometimes just a 'script' """
"""A file teeth.sh in your home directory has been prepared for you, but contains some blanks. Use Nano to edit the file and replace the 
two ____ placeholders with seasonal/*.csv and -c so that this script prints a count of the number of times each tooth name appears in the CSV
files in the seasonal directory."""
# $ nano teeth.sh
# $ bash teeth.sh > teeth.out
# $ cat teeth.out
# out | 15 bicuspid
#       31 canine
#       18 incisor
#       11 molar
#       17 wisdom



## How can I pass filenames to scripts?
"""Edit the script count-records.sh with Nano and fill in the two ____ placeholders with $@ and -l (the letter) respectively so that it counts the number of lines
in one or more files, excluding the first line of each."""
""" >>>>>> $@ === pass filenames to scripts."""
# $ nano cout-records.sh
# tail -q -n +2 $@ | wc -l
# (save and close)
# $ bash count-records.sh  seasonal/*.csv > num-records.out



## How can I process a single argument?
""" >>>>>> $1, $2, and so on === to refer to specific command-line parameters."""
"""---
bash get-field.sh seasonal/summer.csv 4 2
should select the second field from line 4 of seasonal/summer.csv. Which of the following commands should be put in get-field.sh to do that?"""
# head -n $2 $1 | tail -n 1 | cut -d , -f $3



## How can one shell script do many things?
"""edit the script range.sh and replace the two ____ placeholders with $@ and -v so that it lists the names and number of lines in all of the files given on 
the command line without showing the total number of lines in all files. (Do not try to subtract the column header lines from the files.)"""
# $ nano range.sh
# wc -l $@ | grep -v total
"""add sort -n and head -n 1 in that order to the pipeline in range.sh to display the name and line count of the shortest file given to it."""
# wc -l $@ | grep -v total | sort -n | head -n 1
