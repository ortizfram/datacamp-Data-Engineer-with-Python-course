"""********************************************************************************************************************
This chapter covers more complex efficiency tips and tricks. You'll learn a few useful built-in modules for writing efficient code and practice 
using set theory. You'll then learn about looping patterns in Python and how to make them more efficient.

Efficiently combining, counting, and iterating
==============================================
// combine pokemon with healthpoits list

        >>>>>>>> zip ===combine lists easily
        
          $$$$$ must be unpacked into a list and print $$$$$$
          combined_zip = zip(names,hp)  (zip object)
          combined_zip_list = [*combined_zip]
          
Collections module
===================

        >>>>>>>> Counter (collections module)
       
          from collections import Counter
          type_counts = Counter(poke_types)
          print(type_counts)
          
 Itertools module  (combinactory generators)
 =================
 
        >>>>>>>> combinations() (itertools module)
        
        poke_types = ['Bug','Fire','Ghost','Grass','Water']
        from itertools import combinations
        comb_obj = combinations(poke_types,2) # list, umber_of_objects_per_group
        combos = [*comb_obj]
        print(combos)
        # [('Bug','Fire'),('Bug','Ghost'),('Bug','Grass')........
********************************************************************************************************************"""
## Combining Pokémon names and types 1

# Combine names and primary_types
names_type1 = [*zip(names, primary_types)]

print(*names_type1[:5], sep='\n')
"""('Abomasnow', 'Grass')
('Abra', 'Psychic')
('Absol', 'Dark')
('Accelgor', 'Bug')
('Aerodactyl', 'Rock')"""

## Combining Pokémon names and types 2

# Combine all three lists together
names_types = [*zip(names,primary_types,secondary_types)]

print(*names_types[:5], sep='\n')
"""('Abomasnow', 'Grass', 'Ice')
('Abra', 'Psychic', nan)
('Absol', 'Dark', nan)
('Accelgor', 'Bug', nan)
('Aerodactyl', 'Rock', 'Flying')"""

## Combining Pokémon names and types 3



