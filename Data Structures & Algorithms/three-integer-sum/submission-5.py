class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        i = 0
        j = i+1
        k = len(nums)-1

        while i < len(nums):
            if nums[i] == nums[i-1] and i>0:
                i += 1
                continue

            k = len(nums)-1
            j = i+1
            while j < k:
                threeSum = nums[i] + nums[j] + nums[k]
                if threeSum > 0:
                    k -= 1
                elif threeSum < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])

                    k -= 1
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
            i += 1

        return res