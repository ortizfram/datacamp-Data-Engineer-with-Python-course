"""DEFINING EFFICIENT
---------------------
    - Fast runtime(- time)
    - Minimal resource consumption(- memory)
\\"""
  # Non pythonic
  doubled_numbers= []
  for i in range(len(numbers)):
     doubled_numbers.append(numbers[i]*2)
  # Pythonic
  doubled_numbers= [x * 2 for x in numbers]
#``````````````````````````````````````````````````````````````````````````````````````````````````
"""
Pop quiz: what is efficient
In the context of this course, what is meant by efficient Python code?

    # Code that executes quickly for the task at hand, minimizes the memory footprint and follows Python's coding style principles."""
#``````````````````````````````````````````````````````````````````````````````````````````````````
# A taste of things to come 1== Non-pythonic

 names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
    
# Print the list w/ Non-Pythonic approach
i = 0
new_list= []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1
print(new_list)
#``````````````````````````````````````````````````````````````````````````````````````````````````
# A taste of things to come 2== Pythonic

# Print the list created by looping over the contents of names
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
print(better_list)
#``````````````````````````````````````````````````````````````````````````````````````````````````
