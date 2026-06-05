class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}

        left = 0
        max_count = 0

        for right in range(len(s)):
            seen[s[right]] = 1 + seen.get(s[right], 0)

            length = right - left + 1
            most_freq = max(seen.values())

            replacements = length - most_freq

            while replacements > k:
                seen[s[left]] -= 1
                left += 1

                length = right - left + 1
                most_freq = max(seen.values())
    
                replacements = length - most_freq

            max_count = max(max_count, right - left + 1)

        return max_count


