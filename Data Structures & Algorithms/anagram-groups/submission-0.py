class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if anagrams.get(sorted_s):
                anagrams[sorted_s].append(s)
            else:
                anagrams[sorted_s] = [s]

        res = []
        for key, item in anagrams.items():
            res.append(item)

        return res
        