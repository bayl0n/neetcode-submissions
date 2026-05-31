public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> dupes = new HashSet<int>();

        for (int i = 0; i < nums.Length; i++) {
            dupes.Add(nums[i]);
        }

        return dupes.Count != nums.Length;
    }
}
