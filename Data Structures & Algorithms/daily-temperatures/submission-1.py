class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # This solution is O(n^2) and O(n)
        res = []

        for i in range(len(temperatures)):
            count = 0
            j = i+1
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    count = j - i
                    break
                j += 1

            res.append(count)

        return res