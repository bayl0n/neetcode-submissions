class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}

        left = 0
        max_count = 0
        most_freq = 0

        for right in range(len(s)):
            seen[s[right]] = 1 + seen.get(s[right], 0)

            most_freq = max(most_freq, seen[s[right]])

            while (right - left + 1) - most_freq > k:
                seen[s[left]] -= 1
                left += 1

            max_count = max(max_count, right - left + 1)

        return max_count


