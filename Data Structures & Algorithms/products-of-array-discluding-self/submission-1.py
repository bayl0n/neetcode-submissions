class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = []
        res = []

        product = 1
        for num in nums:
            product *= num
            prefix.append(product)

        product = 1
        for num in reversed(nums):
            product *= num
            postfix.append(product)
        postfix.reverse()
        postfix.append(1)

        print(prefix, postfix)

        for i, num in enumerate(nums):
            res.append(prefix[i]*postfix[i+1])

        return res
        
        # res = []
        # for i, num1 in enumerate(nums):
        #     product = 1
        #     for j, num2 in enumerate(nums):
        #         if i == j:
        #             continue
        #         product *= num2

        #     res.append(product)

        # return res
                