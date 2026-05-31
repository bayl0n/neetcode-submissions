class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for key in dict(sorted(count.items(), key=lambda c: c[1], reverse=True)):
            res.append(key)

        return res[:k]