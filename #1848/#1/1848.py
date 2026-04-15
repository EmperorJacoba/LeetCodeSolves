import math # Added before I remembered that max() is not math.max() (as it is in C#)

class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        l = start
        r = start

        while True:
            if nums[l] == target:
                return abs(l - start)
            if nums[r] == target:
                return abs(r - start)

            l = max(l - 1, 0)
            r = min(r + 1, len(nums) - 1)