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

"""
# Create three variables from the temp data files' contents
temp_a=$(cat temps/region_A)
temp_b=$(cat temps/region_B)
temp_c=$(cat temps/region_C)

# Print out the three variables
echo "The three temperatures were $temp_a, $temp_b, and $temp_c"


repl:~/workspace$ bash script.sh
The three temperatures were 34, 36, and 4.2

"""
ARRAYS In BASH

$$$ BASH DOES NOT USE COMMA SEPARATORS $$$

*** Create Array in Bash : 
    - Numerical-indexed : >>>>>> declare -a my_first_array
                          or
                          >>>>>> my_first_array=(1 2 3) 
*** Returning arrays

        # Array syntax                      
        my_array=(10 20 30 44)     

        *** return COMPLETE array : 
            >>>>>> echo ${my_array[@]} 
                   10 20 30 44

        *** return array LENGHT :
            >>>>>> echo ${#my_array[@]}
                   4

        *** Access array ELEMENTS : 
            >>>>>> echo ${my_array[2]}
                   30
               
*** Manipulating arrays

        my_array=(100 113 240 555 66) 

        *** Changing elements :
        >>>>>> my_array[1]=999
               echo ${my_array[1]}
               999

        *** SLICING:
        >>>>>> array[@]:N:M    === N:Starting index, M:How many elem return
        eg:     echo ${my_array[@]:1:3}
                113 240 555

        *** Appending to Array:
            >>>>>> array+=(elements)
            eg:  my_array+=(10)
                 echo ${my_array[@]}
                 100 113 240 555 66 10
                 
*** Associative array (KAY_VALUE)
        a Dictionary in python 

        # first declare
        declare -a city_details 

        # now fill
        city_details=([c_name]='NY' [Population]=1400000)

        # or single line 
        declare -A city_details=([keys]=values)

        # index using keys to return value
        echo ${city_details[c_name]}
        NY
    
        *** Access KEYS (!)
            >>>>>> echo ${!citydetails[@]}
            c_nama Population
"""

"""
### Creating an array

Instructions 1/3

- Create a normal array called capital_cities which contains the cities Sydney, Albany and Paris. Do not use the declare method;
   fill the array as you create it. Be sure to put double quotation marks around each element!
"""
# Create a normal array with the mentioned elements
capital_cities=("Sydney" "Albany" "Paris")
"""
Instructions 2/3

- Create a normal array called capital_cities. However, use the declare method to create in this exercise.
- Below, add each city, appending to the array. The cities were Sydney, Albany, and Paris. Remember to use double quotation marks.
"""
# Create a normal array with the mentioned elements using the declare method
# Create a normal array with the mentioned elements using the declare method
declare -a capital_cities

# Add (append) the elements
capital_cities+=("Sydney")
capital_cities+=("Albany")
capital_cities+=("Paris")
"""
Instructions 3/3

- Now you have the array created, print out the entire array using a special array property.
- Then print out the length of the array using another special property.
"""
# The array has been created for you
capital_cities=("Sydney" "Albany" "Paris")

# Print out the entire array
echo ${capital_cities[@]}

# Print out the array length
echo ${#capital_cities[@]}
    
"""
### Creating associative arrays

Instructions 1/3

In this exercise we will practice creating and adding to an associative array. 
We will then access some special properties that are unique to associative arrays. 
"""
# Create empty associative array
declare -A model_metrics

# Add the key-value pairs
model_metrics[model_accuracy]=98
model_metrics[model_name]="knn"
model_metrics[model_f1]=0.82
"""
Instructions 2/3

- Create the same associative array (model_metrics) all in one line. (model_accuracy, 98), (model_name, "knn"), (model_f1, 0.82). 
   Remember you must add square brackets* around the keys!
- Print out the array to see what you created.
"""
# Declare associative array with key-value pairs on one line
declare -A model_metrics=([model_accuracy]=98 [model_name]="knn" [model_f1]=0.82)

# Print out the entire array
echo ${model_metrics[@]}
"""
Instructions 3/3

- Now that you've created an associative array, print out just the keys of this associative array.
"""
# An associative array has been created for you
declare -A model_metrics=([model_accuracy]=98 [model_name]="knn" [model_f1]=0.82)

# Print out just the keys
echo ${!model_metrics[@]}

"""
### Climate calculations in Bash

Instructions

- Create an array with the two temp variables as elements.
- Call an external program to get the average temperature. You will need to sum array elements then divide by 2. Use the scale parameter to ensure this is to 2 decimal places.
- Append this new variable to your array and print out the entire array.
- Run your script.
"""
# Create variables from the temperature data files
temp_b="$(cat temps/region_B)"
temp_c="$(cat temps/region_C)"

# Create an array with these variables as elements
region_temps=($temp_b $temp_c)

# Call an external program to get average temperature
average_temp=$(echo "scale=2; (${region_temps[0]} + ${region_temps[1]}) / 2" | bc)

# Append average temp to the array
region_temps+=($average_temp)

# Print out the whole array
echo ${region_temps[@]}

    
repl:~/workspace$ bash script.sh 
36 4.2 20.10
