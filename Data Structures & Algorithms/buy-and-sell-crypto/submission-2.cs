public class Solution {
    public int MaxProfit(int[] prices) {
        int left = 0;
        int maxProfit = Int32.MinValue;

        for (int right = left; right < prices.Length; right++) {
            int currProfit = prices[right] - prices[left];

            if (prices[right] < prices[left]) {
                left = right;
            }

            maxProfit = Math.Max(maxProfit, currProfit);
        }

        return maxProfit;
    }
}
