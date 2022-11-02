"""
In this chapter, you’ll learn how to create basic string and numeric variables, and perform calculations on these variables. 
You’ll also learn about the magic of a shell-within-a-shell (shell-ception), opening up huge opportunities for advanced scripting.
"""

"""
*** Basic variables in Bash
    >>>>>> var1="moon" : asign a variable
    >>>>>> echo $var : reference variable with notation 
      
      *** single, double, backticks
          >>>>>> 'text'  : literally what's in between
          >>>>>> "$text or `text` o $(text)"  : literally except using [$] and [backticks], just to be printed out
          >>>>>> `text`  : runs and captures STDOUT back into variable
          
          eg: var="the day is `date`"
              echo $var
              
              the day is 02/11/22 16:51
              
"""

"""
### Using variables in Bash

-Create a variable, yourname that contains the name of the user. Let's use the test name 'Sam' for this.
-Fix the echo statement so it prints the variable and not the word yourname.
-Run your script.

"""
# Create the required variable
yourname="Sam"

# Print out the assigned name (Help fix this error!)
echo "Hi there $yourname, welcome to the website!"


repl:~/workspace$ bash script.sh
Hi there Sam, welcome to the website!

"""
### Shell within a shell
 
-Which of the following correctly uses a 'shell within a shell' to print out the date? 
  We do not want to select the option that will just print out the string 'date'.
  
Answer : echo "Right now it is `date`"

"""

"""
### Numeric variables in Bash

*** for num vars we must use : 
    >>>>>> expr
    
    eg : expr 5+4
         9
         
    *** expr LIMITATIONS : don't handle decimals
*** for decimal vars :
    >>>>>> bc (basic calculator)
    
    eg: 
        # echoing and piping bc
        echo "5 + 7.5" | bc
        12.5
        
        # echo calculation piped to bc for filling string results
        model1=87.65
        model2=89.20
        echo "Score is $(echo "model1 + model2" | bc)"
        score is 176.85
        
*** for specifying decimal places : 
    >>>>>> scale
    
    eg: echo "scale=3; 10/3" | bc
        3.333
"""

"""
### Converting Fahrenheit to Celsius

-Your task is to write a program that takes in a single number (a temperature in Fahrenheit) as an ARGV argument, converts it to 
 Celsius and returns the new value. There may be decimal places so you will need to undertake calculations using the bc program.
-At all times use 2 decimal places using the scale command for bc.
-The formula for Fahrenheit to Celsius is:

The formula for Fahrenheit to Celsius is:
C = (F - 32) x (5/9)

"""
# Get first ARGV into variable
temp_f=$1

# Subtract 32
temp_f2=$(echo "scale=2; $temp_f - 32" | bc)

# Multiply by 5/9
temp_c=$(echo "scale=2; $temp_f2 * 5 / 9" | bc)

# Print the celsius temp
echo $temp_c


repl:~/workspace$ bash script.sh 108
42.22

"""
### Extracting data from files

Your task is to extract the data from each file (by concatenating) into the relevant variable and print it out. 
The temperature in the file region_A needs to be assigned to the variable temp_a and so on.

-Create three variables from the data in the three files within temps by concatenating the content into a variable using a shell-within-a-shell.
-Print out the variables to ensure it worked.
-Save your script and run from the command line.
