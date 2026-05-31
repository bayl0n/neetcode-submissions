class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}

        for c in s:
            s_freq[c] = 1 + s_freq.get(c, 0)

        for c in t:
            t_freq[c] = 1 + t_freq.get(c, 0)

        return s_freq == t_freq