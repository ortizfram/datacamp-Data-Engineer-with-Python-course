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
