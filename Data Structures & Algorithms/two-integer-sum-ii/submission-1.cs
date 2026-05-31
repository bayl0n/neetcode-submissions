public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        var left = 0;
        var right = numbers.Length - 1;

        while (left < right) {
            var currSum = numbers[left] + numbers[right];

            if (currSum == target) {
                return new int[] {left + 1, right + 1};
            } else if (currSum < target) {
                left++;
            } else {
                right--;
            }
        }

        return new int[] {-1, -1};
    }
}
