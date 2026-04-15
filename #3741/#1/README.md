Solved 4/14/26 w/ Python3

First iterates through the list to generate a hashmap of `{<element>: \[<index0>, <index1>...] }`.
Then generates a hashmap of `{<element> : <minimum distance calculation>}` where `<minimum distance calculation>` is as defined
in the problem statement. 

Second hashmap generation calculates the distance for each triad of possible minimized distance values in the list of indeces. For example,
list `[0,3,4,11,19]` would test `0,3,4`, `3,4,11`, and `4,11,19`. The minimum distance of the combinations is what is stored in the hashmap.

Returns the minimum of the second hashmap's values, or `-1` if the second hashmap is empty.

The second hashmap does not need to exist. It can be replaced with one value that stores the current minimum distance calculation, as
that is all that is required by the problem statement. However, if the problem statement was modified to also require return of
the exact value that has the minimum triad difference, this would be able to satisfy that requirement with minimal modification of line 25.

O(n) time, O(n) space.