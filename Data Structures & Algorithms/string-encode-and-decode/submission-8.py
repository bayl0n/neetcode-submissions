class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "$" + s

        return res

    def decode(self, s: str) -> List[str]:
        right = 0
        res = []

        while right < len(s):
            num = ""
            while s[right].isdigit():
                num += s[right]
                right += 1

            if s[right] == "$":
                right += 1

            word = ""
            for i in range(int(num)):
                word += s[right+i]

            right += int(num)
            res.append(word)

        return res



