class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "[": "]",
            "{": "}",
            "(": ")",
        }

        stack = []

        for c in s:
            if c in brackets:
                # deal with it later
                stack.append(c)
            else:
                # refer to our stack
                if len(stack) == 0:
                    return False

                pair = stack.pop()

                if c != brackets[pair]:
                    return False

        return len(stack) == 0



