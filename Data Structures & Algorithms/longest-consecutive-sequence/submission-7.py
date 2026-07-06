class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        To find the longest consecutive sequence, we need to start counting from the start of a sequence.

        In order to determine if a number is the start of a sequence, we can use a set and ask if either
        the number before (or after in this solution) exists in the set.
        If we are counting up (2,3,4,5,6 for example) then we check if 1 exists.
        If we are counting down (6,5,4,3,2) we check if 7 exists in the set.

        Since in both those cases they don't exist, we know that the start of the sequence is 2 (ascending) or 6 (descending)

        We can then start counting from the start of the sequence and loop until we reach the end of it, which we
        know is when the current number (num + current count for asc, num - current for desc).

        Once we have finished counting the sequence, then we can compare it to the max count to see
        if it is the longest sequence.
        """
        num_set = set(nums)
        count = 0

        for num in num_set:
            if num + 1 not in num_set:
                length = 1

                while (num-length) in num_set:
                    length += 1

                count = max(count, length)

        return count