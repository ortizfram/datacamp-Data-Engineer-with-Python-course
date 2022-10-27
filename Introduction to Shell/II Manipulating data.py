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





