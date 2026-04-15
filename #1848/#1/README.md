Solved 4/14/26 w/ Python3



Uses two pointers that expand outward from the target to find the minimum distance. Iterates over as few items in the array as a result.



Technically, l and r don't have to be defined separately. A single variable could be used to define the distance from the start and then return that number upon a find. Lines 5, 6, 14 and 15 could be omitted in this case although there would have to be extra checks to prevent accessing values out of bounds, and would be less readable, in my opinion (although not by much).



O(n) time, O(1) space.

