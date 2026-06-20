public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        var i = 0;
        var j = numbers.Length - 1;

        while (i < j) {
            var currSum = numbers[i] + numbers[j];

            if (currSum == target) {
                return new int[] { i + 1, j + 1 };
            } else if (currSum < target) {
                i++;
                while (i < numbers.Length - 1 && numbers[i] == numbers[i+1]) {
                    i++;
                }
            } else {
                j--;
                while (j > 0 && numbers[j] == numbers[j-1]) {
                    j--;
                }
            }
        }

        return new int[] { -1, -1 };
    }
}
