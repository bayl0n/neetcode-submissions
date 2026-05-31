public class Solution {
    public List<List<int>> ThreeSum(int[] nums) {
        var res = new List<List<int>>();
        Array.Sort(nums);

        for (int i = 0; i < nums.Length; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            if (nums[i] > 0) break;

            int j = i+1;
            int k = nums.Length - 1;

            while (j < k) {
                Console.WriteLine($"{i}, {j}, {k}");

                var threeSum = nums[i] + nums[j] + nums[k];

                if (threeSum == 0) {
                    res.Add(new List<int>() { nums[i], nums[j], nums[k] });
                    j++;
                    k--;

                    while (j < nums.Length && nums[j] == nums[j-1]) {
                        j++;
                    }
                } else if (threeSum < 0) {
                    j++;
                } else {
                    k--;
                }
            }
        }

        return res;
    }
}
