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

# Combine five items from names and three items from primary_types
differing_lengths = [*zip(names[:5], primary_types[:3])]

print(*differing_lengths, sep='\n')
"""('Abomasnow', 'Grass')
('Abra', 'Psychic')
('Absol', 'Dark')"""

# $$$$$ zip() with objects of differing lengths, it will only combine until the smallest lengthed object is exhausted $$$$$
#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
## Counting Pokémon from a sample

# Collect the count of primary types
type_count = Counter(primary_types)
print(type_count, '\n')

# Collect the count of generations
gen_count = Counter(generations)
print(gen_count, '\n')

# Use list comprehension to get each Pokémon's starting letter
starting_letters = [name[0] for name in names]

# Collect the count of Pokémon for each starting_letter
starting_letters_count = Counter(starting_letters)
print(starting_letters_count)
"""Counter({'Water': 66, 'Normal': 64, 'Bug': 51, 'Grass': 47, 'Psychic': 31, 'Rock': 29, 'Fire': 27, 'Electric': 25, 'Ground': 23, 'Fighting': 23, 'Poison': 22, 'Steel': 18, 'Ice': 16, 'Fairy': 16, 'Dragon': 16, 'Ghost': 13, 'Dark': 13}) 

Counter({5: 122, 3: 103, 1: 99, 4: 78, 2: 51, 6: 47}) 

Counter({'S': 83, 'C': 46, 'D': 33, 'M': 32, 'L': 29, 'G': 29, 'B': 28, 'P': 23, 'A': 22, 'K': 20, 'E': 19, 'W': 19, 'T': 19, 'F': 18, 'H': 15, 'R': 14, 'N': 13, 'V': 10, 'Z': 8, 'J': 7, 'I': 4, 'O': 3, 'Y': 3, 'U': 2, 'X': 1})"""
"""!!!
The sample's most common Pokémon type was 'Water' and the sample's least common Pokémon
types were 'Ghost' and 'Dark'. Did you also notice that most of the Pokémon in the sample came from generation 5 and had a starting letter of 'S'?"""
#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
## Combinations of Pokémon

# Import combinations from itertools
from itertools import combinations

# Create a combination object with pairs of Pokémon
combos_obj = combinations(pokemon, 2)
print(type(combos_obj), '\n')

# Convert combos_obj to a list by unpacking
combos_2 = [*combos_obj]
print(combos_2, '\n')

# Collect all possible combinations of 4 Pokémon directly into a list
combos_4 = [*combinations(pokemon,4)]
print(combos_4)
"""<class 'itertools.combinations'> 

[('Geodude', 'Cubone'), ('Geodude', 'Lickitung'), ('Geodude', 'Persian'), ('Geodude', 'Diglett'), ('Cubone', 'Lickitung'), ('Cubone', 'Persian'), ('Cubone', 'Diglett'), ('Lickitung', 'Persian'), ('Lickitung', 'Diglett'), ('Persian', 'Diglett')] 

[('Geodude', 'Cubone', 'Lickitung', 'Persian'), ('Geodude', 'Cubone', 'Lickitung', 'Diglett'), ('Geodude', 'Cubone', 'Persian', 'Diglett'), ('Geodude', 'Lickitung', 'Persian', 'Diglett'), ('Cubone', 'Lickitung', 'Persian', 'Diglett')]"""
"""!!!
combinations() allows you to specify any size of combinations by passing an integer
as the second argument. Ash has 10 combination options when his Pokédex can store only two Pokémon.
He has 5 combination options when his Pokédex can store four Pokémon."""

"""*********************************************************************************************************************
Set theory
===========
        - Applied to collections of objects
        >>>>>>>>>> sets
               0 >>>>>>>>>in 
               1 >>>>>>>>>>intersection()  2 >>>>>>>>>>difference() 3 >>>>>>>>>>symmetric_difference()  4 >>>>>>>>>>union()
                
                0 -> if value exists in a sequence
                1 -> all elements that are in both sets
                2 -> all elements in one set but not in other 
                3 -> all elems in exactly one set---all differences of both together
                4 -> all elems that are in either set--- deletes duplicates, merges uniques
                
      $$$$$ fisrt convert the list into a set $$$$$$ 
      list_a = [1,2,3,4]
      list_b = [5,6,7,4]
      
      list_a = set(lsit_a)
      list_b = set(list_b)
      set_a.intersection(list_b)
      # {4}
      set_a.difference(set_b)
      # {1,2,3}
      set_a.symmetric_difference(set_b)
      # {1,2,3,5,6,7}
      set_a.union(set_b)
      # {1,2,3,4,5,6,7}
*********************************************************************************************************************"""
## Comparing Pokédexes

# Convert both lists to sets
ash_set = set(ash_pokedex)
misty_set = set(misty_pokedex)

# Find the Pokémon that exist in both sets
both = ash_set.intersection(misty_set)
print(both, '\n')

# Find the Pokémon that Ash has and Misty does not have
ash_only = ash_set.difference(misty_set)
print(ash_only, '\n')

# Find the Pokémon that are in only one set (not both)
unique_to_set = ash_set.symmetric_difference(misty_set)
print(unique_to_set, '\n')
"""{'Squirtle', 'Psyduck'} 

{'Koffing', 'Zubat', 'Rattata', 'Spearow', 'Vulpix', 'Wigglytuff', 'Pikachu', 'Bulbasaur'} 

{'Koffing', 'Zubat', 'Spearow', 'Vulpix', 'Rattata', 'Wigglytuff', 'Tentacool', 'Slowbro', 'Krabby', 'Bulbasaur', 'Pikachu', 'Poliwag', 'Magikarp', 'Vaporeon', 'Starmie', 'Horsea'} """
"""!!!
you were able to see that both Ash and Misty have 'Psyduck' and 'Squirtle' in their Pokédex.
You were also able to see that Ash has 8 Pokémon that Misty does not have."""
#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
