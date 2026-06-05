# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.sort(pairs)
    
    def sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = (len(arr)) // 2

        arr1 = self.sort(arr[:mid])
        arr2 = self.sort(arr[mid:])

        res = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i].key <= arr2[j].key:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1

        while i < len(arr1):
            res.append(arr1[i])
            i += 1

        while j < len(arr2):
            res.append(arr2[j])
            j += 1

        return res

