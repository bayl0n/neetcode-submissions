class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i, num1 in enumerate(nums):
            product = 1
            for j, num2 in enumerate(nums):
                if i == j:
                    continue
                product *= num2

            res.append(product)

        return res
                