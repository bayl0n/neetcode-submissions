public class Solution {
    public int LongestConsecutive(int[] nums) {
        var numSet = new HashSet<int>();
        var count = 0;

        foreach (var num in nums) {
            numSet.Add(num);
        }

        foreach (var num in numSet) {
            if (!numSet.Contains(num-1)) {
                var length = 0;

                while (numSet.Contains(num + length)) {
                    length++;
                }

                count = Math.Max(count, length);
            }
        }

        return count;
    }
}
