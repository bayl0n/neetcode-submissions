public class Solution {
    public List<List<int>> ThreeSum(int[] nums) {
        var res = new List<List<int>>();

        var sortedNums = (int[])nums.Clone();
        Array.Sort(sortedNums);

        Console.WriteLine(string.Join(", ", sortedNums));

        for (int i = 0; i < sortedNums.Length; i++) {
            if (sortedNums[i] > 0) break;
            if (i > 0 && sortedNums[i] == sortedNums[i - 1]) continue;

            int j = i+1;
            int k = sortedNums.Length-1;

            while (j < k) {
                var currSum = sortedNums[i] + sortedNums[j] + sortedNums[k];

                Console.WriteLine($"{sortedNums[i]} + {sortedNums[j]} + {sortedNums[k]} = {currSum}");

                if (currSum == 0) {
                    res.Add(new List<int>() {sortedNums[i], sortedNums[j], sortedNums[k]});

                    j++;
                    k--;
                    while (j < k && sortedNums[j] == sortedNums[j - 1]) {
                        j++;
                    }
                } else if (currSum < 0) {
                    j++;
                } else {
                    k--;
                }
            }
        }

        return res;
    }
}
