class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = set()

        for num in nums:
            n.add(num)

        return len(n) != len(nums)