public class Solution {
    public int FindMin(int[] nums) {
        var left = 0;
        var right = nums.Count() - 1;

        while (left < right)
        {
            var mid = left + (right - left) / 2;

            if (nums[mid] > nums[right])
            {
                // We know the array is rotated and the min could be to the right
                left = mid + 1;
            }
            else
            {
                right = mid;
            }
        }

        return nums[left];
    }
}
