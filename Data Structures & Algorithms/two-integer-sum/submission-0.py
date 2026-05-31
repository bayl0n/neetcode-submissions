class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}

        for i, num in enumerate(nums):
            if target - num not in compliments:
                compliments[num] = i;
            else:
                return [compliments[target - num], i]