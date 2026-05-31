class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        count = 0

        l = 0
        r = l + 1
        pos = {s[l]: l}
        while r < len(s):
            if pos.get(s[r]):
                pos = {}
                l += 1
                r += 1
            else:
                pos[s[r]] = r
                r += 1

            count = max(len(pos), count)

        return count