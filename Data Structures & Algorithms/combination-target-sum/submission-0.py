class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(arr, curr, index):
            if curr == target and index < len(nums):
                res.append(arr[:])
                return

            for i in range(index, len(nums)):
                if nums[i] + curr > target:
                    continue

                arr.append(nums[i])
                dfs(arr, curr + nums[i], i)
                arr.pop()
        
        dfs([], 0, 0)

        return res