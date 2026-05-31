class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        wd = len(digits)-1

        while wd >= 0:
            digits[wd] += 1
            digits[wd] %= 10

            if digits[wd] == 0:
                if wd == 0:
                    digits.insert(0, 1)
                    break
                else:
                    wd -= 1
                    continue
            else:
                break

        return digits





