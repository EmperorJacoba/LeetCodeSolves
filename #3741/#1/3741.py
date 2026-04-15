class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        d = dict()

        for index, element in enumerate(nums):
            if element in d.keys():
                d[element].append(index)
            else:
                d[element] = [index]

        maxes = dict()
        for i in d:
            if len(d[i]) < 3:
                continue
            else:
                current_min = float("infinity")
                for j in range(len(d[i]) - 2):
                    calculated = abs(d[i][j] - d[i][j + 1]) + abs(d[i][j + 1] - d[i][j + 2]) + abs(d[i][j + 2] - d[i][j])
                    current_min = min(current_min, calculated)
                maxes[i] = current_min

        if len(maxes) == 0:
            return -1

        return min(maxes.values())