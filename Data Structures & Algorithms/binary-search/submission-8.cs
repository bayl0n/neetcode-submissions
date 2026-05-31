public class Solution {
    public int Search(int[] nums, int target) {
        /*
        Ascending order (non-decreasing) 0, 4, 1, 2, 1
        -> 0, 1, 1, 2, 4
        */

        int left = 0;
        int right = nums.Length - 1;

        while(left <= right) {
            // int midpoint = (left + right) / 2; // bad because of integer overflow
            int midpoint = left + ((right - left) / 2);

            if (nums[midpoint] == target) {
                return midpoint;
            }
            else if(nums[midpoint] < target) {
                left = midpoint + 1;
            }
            else {
                right = midpoint - 1;
            }
        }

        return -1;
    }
}
