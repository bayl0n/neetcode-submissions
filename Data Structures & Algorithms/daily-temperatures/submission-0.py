class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for i in range(len(temperatures)):
            count = 0
            j = i+1
            while j < len(temperatures):
                if temperatures[i] < temperatures[j]:
                    count = j - i
                    break
                j += 1

            res.append(count)

        return res