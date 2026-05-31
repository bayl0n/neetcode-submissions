class Solution:
    def reverseBits(self, n: int) -> int:
        # 1010010000000000
        # 0000000000100101
        res = 0

        """
        ^   -   0 ^ 1 = 1, 
        &
        |
        ~
        >>
        <<

        1010010000000000
        0101101111111111
        """
        res = 0

        for i in range(32):
            current_bit = ((n >> i) & 1)

            res += (current_bit << (31 - i))

        return res