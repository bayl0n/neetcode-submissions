public class Solution {
    public int Search(int[] nums, int target) {
        var left = 0;
        var right = nums.Count() - 1;

        while (left <= right) {
            var mid = (right + left) / 2;

            if (nums[mid] > target) {
                right = mid - 1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                return mid;
            }
        }

        return -1;
    }
}
