"""
This chapter will show you how to work with the data in those files. The tools we’ll use are fairly simple, but are solid building blocks.
"""

## How can I view a file's contents?
""" >>>>>> cat === quick view of contents."""
# $ cat course.txt
"""Introduction to the Unix Shell for Data Science......"""


## How can I view a file's contents piece by piece?
""" >>>>>> less === one page at a time, passing with [SPACE], leaving with [q]
    >>>>>> :n  , :p  === next and previous file when using less.
    >>>>>> :q  === quit."""
# $ less seasonal/spring.csv seasonal/summer.csv
# :n
# :p
# :q


## How can I look at the start of a file?
""" >>>>>> head === look at the start of a file."""
# $ head people/agarwal.txt
# | Display as many lines as there are.


## How can I type less?
""" >>>>>> [TAB] === autocompletition"""
"""Run head seasonal/autumn.csv without typing the full filename."""
# $ head seasonal/autumn.csv  
# $ head seasonal/spring.csv


## How can I control what commands do?
"""FLAGS
---------"""
""" >>>>>> head -n 10 === first 10 results."""
# $ head -n 5 seasonal/winter.csv


## How can I list everything below a directory?
""" >>>>>> ls -R  === see every file and directory in the current level, then everything in each sub-directory.
    >>>>>> ls -F === puts '/' after a directory. puts '*' after runnable program."""
# $ ls -R -F.:
"""backup/  bin/  course.txt  people/  seasonal/
    ./backup:

    ./bin:

    ./people:
    agarwal.txt

    ./seasonal:
    autumn.csv  spring.csv  summer.csv  winter.csv"""


## How can I get help for a command?
""" >>>>>> man === (maual) find out what commands DO.---invokes 'less', use [SPACE] to see more [q] to quit"""
# $ man tail   [SPACE][q]
# $ tail -n +7 seasonal/spring.csv


## How can I select COLUMNS from a file?
""" >>>>>> cut === select columns."""
         # cut -f 2-5,8 -d , values.csv
                     #-f(specify columns), -d(delimiter to specify the separator)--because some files may use spaces, tabs, or colons
"""---What command will select the first column (containing dates) from the file spring.csv?"""
"""cut -d , -f 1 seasonal/spring.csv
    cut -d, -f1 seasonal/spring.csv"""
# Either of the above.


## What can't cut do?
"""---What is the output of cut -d : -f 2-4 on the line:"""
# second:third:
# |  The trailing colon creates an empty fourth field.


## How can I repeat commands?
""" >>>>>> history === see latest command history."""
# $ head summer.csv
# $ cd seasonal/
# $ !head
"""head summer.csv
Date,Tooth
2017-01-11,canine
2017-01-18,wisdom
2017-01-21,bicuspid
2017-02-02,molar....."""
# $ history
"""   1  head summer.csv
    2  cd seasonal/
    3  head summer.csv
    4  history"""
