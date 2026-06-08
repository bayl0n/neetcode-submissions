class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def search(curr, index):
            if index == len(nums):
                res.append(curr[:])
                return

            curr.append(nums[index])

            search(curr, index + 1)

            curr.pop()

            search(curr, index + 1)

        search([], 0)

        return res