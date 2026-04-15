Solved 12/18/25 w/ Python3

Converts the number to a string and then to a list of characters. Reverses the list with `.reverse()`, and checks to see if the last char
is a negative sign. If so, preserves the negative number by moving it to the beginning.

Recreates a string from the list of characters, and then casts to int. Checks to see if it exceeds the 32-bit integer limit
and returns 0 if that is the case (as that is required by the problem statement), otherwise returns the reversed integer.

This solution is a bit clunky, as the conversion to a string and then to a list is largely unnecessary and could be simplified
(as is shown by many of the top solutions). Additionally, the integer limit can be checked pre-reverse to save some computing
power. 

O(n) space, O(n) time.