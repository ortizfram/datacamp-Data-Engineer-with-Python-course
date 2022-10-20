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
