class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        The slowest rate of bananas Koko can eat is 1

        The fastest rate of bananas Koko can eat is max(piles)

        As we need the slowest rate that fits K, rather than linearly
        searching through each integer, we can instead use binary
        search starting from the middle of 1 and K and check
        if that integer is valid
        """
        lower_bound = 1
        upper_bound = max(piles)
        res = upper_bound

        while lower_bound <= upper_bound:
            mid = (lower_bound + upper_bound) // 2

            kTime = self.checkSpeed(mid, piles)
            if kTime <= h:
                res = min(res, mid)
                upper_bound = mid-1
            else:
                lower_bound = mid+1
        return res
        
    def checkSpeed(self, k: int, piles: List[int]) -> int:
        count = 0
        for b in piles:
            hours = math.ceil(b / k)
            count += hours
        return count