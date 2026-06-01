class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = list(nums)

        for num in nums:
            ans.append(num)

        return ans