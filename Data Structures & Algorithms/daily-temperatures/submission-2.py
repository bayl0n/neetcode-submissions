class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        stack = []

        for i, temp in enumerate(temperatures):
            if not stack: # check for other conditions later
                stack.append([temp, i])
            else:
                print(stack)
                if temp > stack[-1][0]:
                    while stack and temp > stack[-1][0]:
                        curr = stack.pop()
                        res[curr[1]] = i - curr[1]
                
                stack.append([temp, i])

            res.append(0)
        return res