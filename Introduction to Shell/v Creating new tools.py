"""
History lets you repeat things with just a few keystrokes, and pipes let you combine existing commands to create new ones. In this chapter,
you will see how to go one step further and create new commands of your own.
"""

## How can I edit a file?
"""text editor Nano. If you type 
      >>>>>> nano filename === it will open/create filename for editing
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
""" >>>>>> cp -h === dont print filenames."""
