class Solution:
    def reverse(self, x: int) -> int:
        str_int = list(str(x))
        str_int.reverse()
        if (str_int[-1] == "-"):
            str_int.insert(0, "-")
            str_int.pop()
        str_as_int = int("".join(str_int))
        if (str_as_int > 2 ** 31 - 1 or str_as_int < - (2 ** 31)):
            return 0
        return str_as_int