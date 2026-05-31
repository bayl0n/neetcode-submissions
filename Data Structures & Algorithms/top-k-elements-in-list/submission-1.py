class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums)+1)]
        count = {}
        res = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for c in count:
            buckets[count[c]].append(c)

        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
            
        
        # count = {}
        # res = []

        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)

        # for key in dict(sorted(count.items(), key=lambda c: c[1], reverse=True)):
        #     res.append(key)

        # return res[:k]