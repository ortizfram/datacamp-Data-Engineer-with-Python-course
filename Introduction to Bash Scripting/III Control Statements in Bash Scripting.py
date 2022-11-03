"""
 You’ll learn the differences between FOR, WHILE, IF, and CASE statements and how to use them in your Bash scripts.
 Armed with these new tools, you’ll be ready to create more advanced Bash scripts with conditional logic.
 """
"""
*** IF statements

    *** sytax
       >>>>>> if [ condition ]; then 
                  # some code
              else
                  # some other code
              fi   

     # double parethesis structure
     eg:     
        if (($x > 5)); then
            echo "$x is more than 5!"
        fi    

     # square brackets and arithmetic flags structure
       >>>>>> -eq : 'equal to'
       >>>>>> -ne : 'not equal to'
       >>>>>> -lt : 'less than'
       >>>>>> -le : 'less than or equal to'

       eg: 
          if [ $x -gt 5 ]; then
              echo "$x is grater than 5!"
          fi
         
*** bash Conditional Flags
    >>>>>> -e : 'file exists'
    >>>>>> -s : 'if exists and it's grater than zero'
    >>>>>> -r : 'if exists and readable'
    >>>>>> -w : 'if exists and writable'
       
*** AND OR in bash
    >>>>>> && : 'and'
    >>>>>> || : 'or'
       
    eg: 
       # Simple-square notation 
       if [ $x -gt 5 ] && [ $x -lt 11 ]; then
           echo "$x more than 5, less than 11"
       fi

       # Double-square notation
       if [[  $x -gt 5 &&  ]]; then
          echo "$x more than 5, less than 11"
       fi
"""

"""
### Sorting model results

Instructions

- Create a variable, accuracy by extracting the "Accuracy" line (and "Accuracy" value) in the first ARGV element (a file).
- Create an IF statement to move the file into good_models/ folder if it is greater than or equal to 90 using a flag, not a mathematical sign.
- Create an IF statement to move the file into bad_models/ folder if it is less than 90 using a flag, not a mathematical sign.
- Run your script from the terminal pane twice (using bash script.sh). Once with model_results/model_1.txt, then once with model_results/model_2.txt as the 
  only argument.
"""
# Extract Accuracy from first ARGV element
accuracy=$(grep Accuracy $1 | sed 's/.* //')

# Conditionally move into good_models folder
if [ $accuracy -ge 90 ]; then
    mv $1 good_models/
fi

# Conditionally move into bad_models folder
if [ $accuracy -lt 90 ]; then
    mv $1 bad_models/
fi

repl:~/workspace$ bash script.sh model_results/model_1.txt
repl:~/workspace$ bash script.sh model_results/model_2.txt
 
"""
### Moving relevant files

Instructions

- Create a variable sfile out of the first ARGV element.
- Use an IF statement and grep to check if the sfile variable contains SRVM_ AND vpt inside.
- Inside the IF statement, move matching files to the good_logs/ directory.
- Try your script on all of the files in the directory (that is, run it four times - once for each file). It should move only one of them.
"""
# Create variable from first ARGV element
sfile=$1

# Create an IF statement on sfile's contents
if grep -q 'SRVM_' $sfile && grep -q 'vpt' $sfile; then
	# Move file if matched
	mv $sfile good_logs/
fi

repl:~/workspace$ bash script.sh logfiles8.txt
repl:~/workspace$ bash script.sh logdays.txt  
repl:~/workspace$ bash script.sh log1.txt
