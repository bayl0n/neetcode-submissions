class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        points.sort(key = lambda p: math.sqrt(p[0]**2 + p[1]**2))

        for i in range(k):
            res.append(points[i])

        return res