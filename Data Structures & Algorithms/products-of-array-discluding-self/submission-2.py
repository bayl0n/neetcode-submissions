class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        res = []

        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            prefix.append(product)

        product = 1
        for i in range(len(nums)-1, -1, -1):
            product *= nums[i]
            postfix.append(product)

        postfix.reverse()

        for i, num in enumerate(nums):
            left = 1
            right = 1
            if i > 0:
                left = prefix[i-1]

            if i < len(nums)-1:
                right = postfix[i+1]

            res.append(right * left)

        return res