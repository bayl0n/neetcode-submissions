# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.sort(pairs, 0, len(pairs)-1)

        return pairs

    def sort(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr

        i = s
        pivot = arr[e]
        for j in range(s,e):
            if arr[j].key < pivot.key:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1

        arr[e] = arr[i]
        arr[i] = pivot

        self.sort(arr, s, i - 1)
        self.sort(arr, i+1, e)