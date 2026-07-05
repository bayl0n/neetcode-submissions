class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        [3,4,5,6,1,2] 
        1

        left = 3
        right = 5

        mid = 3

        5

        2
        left = mid
        """

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (right + left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
