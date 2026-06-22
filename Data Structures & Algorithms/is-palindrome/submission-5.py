class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitised_s = ''

        for c in s:
            if c.isalnum() and c != ' ':
                sanitised_s += c.lower()

        left = 0
        right = len(sanitised_s) - 1

        while left < right:
            if sanitised_s[left] != sanitised_s[right]:
                return False
            left += 1
            right -= 1

        return True
