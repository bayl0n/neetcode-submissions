class Solution:
    def isHappy(self, n: int) -> bool:
        cycles = set()

        while n not in cycles:
            cycles.add(n)

            nsum = 0
            while n:
                digit = n % 10
                digit = digit**2
                nsum += digit
                n = n // 10
            n = nsum

            if n == 1:
                return True

        return False
        
        