class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr, index):
            if index == len(nums):
                res.append(curr[:])
                return

            # explore if we want to include the current number at index
            curr.append(nums[index])
            backtrack(curr, index+1)

            # explore if we want to not include the current number at index
            curr.pop()
            backtrack(curr, index+1)

        backtrack([], 0)
        return res
