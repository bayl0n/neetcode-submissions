class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        counts = collections.defaultdict(int)
        reference = collections.defaultdict(int)

        left = 0

        # init reference
        for c in t:
            reference[c] += 1
            counts[c] = 0

        have, need = 0, len(reference)
        res, resLen = [-1, -1], math.inf
        left = 0

        for right in range(len(s)):
            curr = s[right]

            counts[curr] += 1

            if curr in reference and counts[curr] == reference[curr]:
                have += 1

            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                counts[s[left]] -= 1

                if s[left] in reference and counts[s[left]] < reference[s[left]]:
                    have -= 1

                left += 1

        left, right = res 

        return s[left:right+1] if resLen != math.inf else ""