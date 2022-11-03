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

"""
*** FOR loops & WHILE 
	 
   *** syntax
	 for z in 1 2 3
	 do 
	    echo $z
	 done

	    # num range 'brace expansion'
	    {START..STOP..INCREMENT}
	    for x in {1..3..2}
	    do
		echo $x
	    done

	    # three expression syntax
		# -double parenthesis
		# -{START..STOP..INCREMENT}
		eg:
		   for ((x=2;x>=4;x+=2))
		   do
		      echo $x
		   done
		   -2
		   -4
		   
	   # glob expansions
	   for book in books/*
	   do 
	   	echo $book
	   done
	   
	   # shell-w/in-a-shell to FOR loop
	   for book in $(ls books/ | grep -i 'air')
	   do
	   	echo $book
	   done
	   -AirportBook.txt
	   -FairMarketBook.txt
	   
*** WHILE
	eg:
	   x=1
	   while [ $x -le 3 ];
	   do 
	   	echo $x
		((x+=1))
	  done		
"""

"""
### A simple FOR loop

Instructions

- Use a FOR statement to loop through files that end in .R in inherited_folder/ using a glob expansion.
- echo out each file name into the console.
"""
# Use a FOR loop on files in directory
for file in inherited_folder/*.R
do  
    # Echo out each file
    echo $file
done

"""
### Correcting a WHILE statement

can you determine where the mistake is? What will happen if it runs?

You can find the code by using cat emp_script.sh to print it to the console.

Instructions

Possible Answers :

 @ There is no mistake, this script will run just fine.
 @ It will run forever because emp_num isn't incremented inside the loop.
 @ You cannot cat a .txt file so this will fail.
 
Answer : It will run forever because emp_num isn't incremented inside the loop.
"""

"""
### Cleaning up a directory

Instructions

- Use a FOR statement to loop through (using glob expansion) files that end in .py in robs_files/.
- Use an IF statement and grep (remember the 'quiet' flag?) to check if RandomForestClassifier is in the file. Don't use a shell-within-a-shell here.
- Move the Python files that contain RandomForestClassifier into the to_keep/ directory.
"""
# Create a FOR statement on files in directory
for file in robs_files/*.py
do  
    # Create IF statement using grep
    if grep -q 'RandomForestClassifier' $file ; then
        # Move wanted files to to_keep/ folder
        mv $file to_keep/
    fi
done


repl:~/workspace$ cd /home/repl/workspace
repl:~/workspace$ bash script.sh
	
"""
*** CASE statements
     *** basic syntax
	>>>>>> case 'something' in
	
        *** regex for pattern
	    >>>>>> Air* : 'starts w/ Air'
	    >>>>>> *hat* : 'contains hat'
	    
	    ***syntax
	    	case 'something' in
			PATTERN1)
			COMMAND1;;
			PATTERN2)
			COMMAND2;;
			*)
			DEFAULT COMMAND;;
		esac
		
	    eg: #new case statement
	    	case $(cat $1) in
		     *Sydney*)
		     mv $1 sydney/ ;;
		     *melbourne*|*brisbane*)
		     rem $1 ;;
		     *canberra*)
		     mv $1 "IMPORTANT_$1" ;;
		     *)
		     echo "no cities found!" ;;
	        esac
"""
	    	
	    	
		
