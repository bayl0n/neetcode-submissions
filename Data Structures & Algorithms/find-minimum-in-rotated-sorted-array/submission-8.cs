public class Solution {
    public int FindMin(int[] nums) {
        var left = 0;
        var right = nums.Count() - 1;

        while (left < right) {
            var mid = (right + left) / 2;

            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return nums[left];
    }
}
