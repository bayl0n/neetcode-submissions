class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        numset = set()

        for num in nums:
            numset.add(num)


        if not numset:
            return count

        minNum = min(numset)

        curr = 0
        while numset:
            if minNum in numset:
                curr += 1
                numset.remove(minNum)
                minNum += 1
            else:
                minNum = min(numset)
                curr = 0
            count = max(curr, count)
                
        return count
        