class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        ans = []

        i = 0

        while i < len(sorted_nums) - 2:
            if i > 0:
                while i < len(sorted_nums) - 2 and sorted_nums[i] == sorted_nums[i-1]:
                    i += 1

            j = i + 1
            k = len(sorted_nums) - 1

            while j < k:
                curr = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]

                if curr == 0:
                    ans.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    j += 1
                    k -= 1
                    while j < k and sorted_nums[j] == sorted_nums[j-1]: j += 1
                    while j < k and sorted_nums[k] == sorted_nums[k+1]: k -= 1
                elif curr < 0:
                        j += 1
                elif curr > 0:
                        k -= 1

            i += 1 
        return ans



