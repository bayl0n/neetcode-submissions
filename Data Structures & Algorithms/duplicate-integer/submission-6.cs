public class Solution {
    public bool hasDuplicate(int[] nums) {
        var uniqueChars = new HashSet<int>();

        foreach (var num in nums) {
            uniqueChars.Add(num);
        }

        return uniqueChars.Count() != nums.Length;
    }
}