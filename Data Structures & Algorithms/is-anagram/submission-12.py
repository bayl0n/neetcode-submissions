class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        solution 1: sort the two arrays and compare equality
        this solution would be O(nlogn)

        solution 2: add each element to a hash set and compare equality
        this would be O(n) where n is the length of s and t (since they
        need to be equal in length)
        """
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)

