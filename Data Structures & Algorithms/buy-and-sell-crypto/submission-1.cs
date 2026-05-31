public class Solution {
    public int MaxProfit(int[] prices) {
        var left = 0;
        var maxProfit = 0;

        for (int right = left; right < prices.Length; right++) {
            var currProfit = prices[right] - prices[left];

            if (prices[right] < prices[left]) {
                left = right;
            }

            maxProfit = Math.Max(maxProfit, currProfit);
        }

        return maxProfit;

        /*
        [10,1,5,6,7,1]

        variables
        --------
        left = 1
        right = 5
        currProfit = 0
        maxProfit = 6
        */
    }
}
