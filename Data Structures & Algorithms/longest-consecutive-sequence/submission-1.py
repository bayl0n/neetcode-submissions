class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        count = 0
        for num in numset:
            if num - 1 not in numset:
                length = 1
                while (num + length) in numset:
                    length += 1
                count = max(length, count)
        return count