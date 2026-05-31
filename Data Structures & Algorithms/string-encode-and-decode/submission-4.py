class Solution:

    def encode(self, strs: List[str]) -> str:
        start = "<"
        end = ">"
        res = ""

        for s in strs:
            res += start + s + end

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        stack = []

        word = ''

        for i in range(len(s)):
            if not stack:
                if s[i] == '<':
                    stack.append('>')
            else:
                if s[i] == stack[0]:
                    stack.pop()
                    res.append(word)
                    word = ''
                else:
                    word += s[i]
        return res

