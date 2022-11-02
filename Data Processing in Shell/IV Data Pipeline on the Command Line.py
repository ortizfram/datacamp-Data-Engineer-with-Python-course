"""~~~
execute Python on the command line, to install dependencies using the package manager pip, and to build an entire model pipeline using the command line.
"""
"""
>>>>>> man python, python -v/--version : prints version num of executable if exists
>>>>>> which python : to see location of py you're using  
>>>>>> python : activate python in terminal, inde only use  python syntax
    >>>>>> exit() : to leave python session from terminal
>>>>>> python hello_world.py : execute python script in command line 

*** Python session :
      easy to activate
      intuitive 
      NOT good for REPRODUCIBILITY
      
    *** Alternative : 
          -Save python command in a [script .py]
          -execute script callig [python + script]
          
        *** How : 
              -create .py file in any editor
              or
              if script is very short: 
              -echoing py syntax into hello_world.py and redirecting into .py file
              
              eg: echo "print('hello world')" > hello_world.py
"""

### Finding Python version on the command line
"""
---Which of the following commands will NOT show what version of Python is installed?
Instructions
50 XP

answer: which python 

which python shows the location where Python is installed on your machine. This does not always contain the version of Python in the folder name.
"""

### Executing Python script on the command line
"""
Here, we will create a Python file and execute it using our native Python, all without leaving the bash terminal.

Instructions
100 XP

-In one step, create a new Python file and pass the Python print command into the file.
-Execute the new Python file by calling it directly from the command line.
"""
# in one step, create a new file and pass the print function into the file
echo "print('This is my first Python script')" > my_first_python_script.py

# check file location 
ls

# check file content 
cat my_first_python_script.py

# execute Python script file directly from command line  
python my_first_python_script.py


"""
Python package installation with pip

*** pip :
     >>>>>> pip install --upgrade pip  : update pip 
     >>>>>> pip list : to see all packages installed in python environment 
     >>>>>> pip install library_name : to install new library package 
          >>>>>> pip install library_name==1.1.1  : to install older version of pip package
          >>>>>> pip install --upgrade library_name  : to update pip package
     >>>>>> pip install library_name name2 name 3 : to install more thanm 1 pip packages
     
     *** automatically download many package sat once 
          -save packages name, 1 package per line in file called [requirements.txt]
          -r : install packages from requirements.txt -as below
          
          eg: pip install -r requirements.txt
"""


"""
### Understanding pip's capabilities

-Which of the following statements regarding pip is NOT true?

Instructions
50 XP

Answer: pip can only install one Python package at a time
"""


"""
### Installing Python dependencies

In this pipeline we will create the requirements.txt file which houses the dependencies we need to install, install the dependencies, 
and do a quick sanity check to make sure everything is properly set up.
      
instructions 1/3
35 XP
1

-Instantiate the requirements.txt document and add the scikit-learn library to the requirements.txt file.
"""
# Add scikit-learn to the requirements.txt file
echo "scikit-learn" > requirements.txt

# Preview file content
cat requirements.txt

# Install the required dependencies
pip install -r requirements.txt

# Verify that Scikit-Learn is now installed
pip list


"""
### Running a Python model

In this exercise, we'll run a pre-written Python script create_model.py which will output two things: a Python model in a saved
.pkl file and the predicted scores in a saved .csv file.

Instructions 1/2
50 XP
1

-Use pip to list and verify that the libraries specified in create_model.py have been installed.
"""
# Re-install requirements
pip install -r requirements.txt

# Preview Python model script for import dependencies
cat create_model.py

# Verify that dependencies are installed
pip list
"""
Instructions 2/2
50 XP
2

-Run the Python script create_model.py from the command line.
"""
# Re-install requirements
pip install -r requirements.txt

# Preview Python model script for import dependencies
cat create_model.py

# Verify that dependencies are installed
pip list

# Execute Python model script, which outputs a pkl file
python create_model.py

# Verify that the model.pkl file has been created 
ls

"""
Data job automation with cron

*** sheduler : runs jobs on predetermined shedule
               allows to automate data pipeline 
               Airflow, Luigi, Rundeck, etc
               
*** CRON scheduler :  -Free
                      -Simple
                      -customizable
                      - purely command-line
                      -native to MAC-os, Linux
                      
                     *** Can be Installed in windows via Cygwin or replaced w/ windows task scheduler
                     
                     *** Used to :
                          automate jobs
                          sys mantenance
                          bash script
                          python jobs
                          
*** Crontab : central file to keep track of cron jobs
    >>>>>> crontab -l :  display all task currently scheduled
    >>>>>> man crontab  : to see documentation 
    
    *** add job to crontab : 
          -echoing into crontab file
          
          eg: echo "* * * * * python create_model.py" | crontab
          
        *** How to time a cron job : 
              * minute (0-59)
              ** hour (0-23)
              *** day of month  (1-31)
              **** month  (1-12)
              ***** day of week (1-7)
"""

"""
### Understanding cron scheduling syntax

-Which of the following is the correct Crontab syntax for execute the Python model script (model.py) every hour, on the 15 minute of an hour?
    (e.g. 12:15 PM, 1:15 AM, 2:15 AM, etc)?
    
Answer : 15 * * * * python model.py
"""


"""
### Scheduling a job with crontab

-Verify that there are currently no CRON jobs currently scheduled via CRONTAB.
"""
# Verify that there are no CRON jobs currently scheduled
crontab -l 

# Create Python file hello_world.py
echo "print('hello world')" > hello_world.py

# Preview Python file 
cat hello_world.py

# Add as job that runs every minute on the minute to crontab
echo "* * * * * python hello_world.py" | crontab

# Verify that the CRON job has been added
crontab -l
