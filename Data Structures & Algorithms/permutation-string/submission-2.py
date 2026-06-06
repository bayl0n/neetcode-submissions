class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        for r in range(len(s1)-1, len(s2)):
            s1_freq = {}
            sub_freq = {}

            for c in s1:
                s1_freq[c] = 1 + s1_freq.get(c, 0)

            for c in s2[l:l+len(s1)]:
                sub_freq[c] = 1 + sub_freq.get(c, 0)

            if s1_freq == sub_freq:
                return True
            
            l += 1

        return False

