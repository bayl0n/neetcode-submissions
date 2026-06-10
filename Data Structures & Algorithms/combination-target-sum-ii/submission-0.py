class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # [] -> 9, 2, 2, 4, 6, 1, 5, -> [2] -> 9, 2, 4, 6, 1, 5 -> [2, 2] -> [9, 4, 6, 1, 5] -> [2, 2, 5]
        # sum = 9
        # if i == index and i < index ==> i <= index

        self.res = []

        candidates.sort()

        def backtrack(index, curr, arr):
            # base case
            if curr == target:
                self.res.append(arr[:])
                return 

            # explore all possible options
            for i in range(index, len(candidates)):
                if candidates[i] + curr > target:
                    break

                if (i > index and candidates[i] == candidates[i-1]):
                    continue

                arr.append(candidates[i])
                backtrack(i+1, curr + candidates[i], arr)
                arr.pop()

        backtrack(0, 0, [])

        return self.res
