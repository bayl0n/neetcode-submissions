public class Solution {
    public bool hasDuplicate(int[] nums) {
        var uniqueNums = new HashSet<int>();

        foreach (var num in nums) {
            if (uniqueNums.Contains(num)) {
                return true;
            }
            else {
                uniqueNums.Add(num);
            }
        }

        return uniqueNums.Count() != nums.Length;
    }
}