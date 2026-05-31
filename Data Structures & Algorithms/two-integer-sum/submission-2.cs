public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        /*
            nums[i] + nums[j] == target?

            [1, 2, 6, 8, -1 5]

            target = 9

            return: [0, 3]

            Dictionary<int, int>() = { 8: 0, }
        */

        var complements = new Dictionary<int, int>();

        for (var i = 0; i < nums.Length; i++) {
            if (complements.ContainsKey(nums[i])) {
                return new int[] { complements[nums[i]], i};
            }
            else {
                complements[target - nums[i]] = i;
            }
        }

        return new int[] { -1, -1};
    }
}
