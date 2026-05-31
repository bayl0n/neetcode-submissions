class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}

        for i, num in enumerate(nums):
            if num in compliments:
                return [compliments[num], i]

            compliments[target - num] = i