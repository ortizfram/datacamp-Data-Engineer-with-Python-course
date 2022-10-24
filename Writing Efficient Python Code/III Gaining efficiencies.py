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
