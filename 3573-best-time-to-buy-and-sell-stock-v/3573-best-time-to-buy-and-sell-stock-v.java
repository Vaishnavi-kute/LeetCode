class Solution {
    public long maximumProfit(int[] prices, int k) {
        int n = prices.length;
        long[] prev = new long[n];
        long[] curr = new long[n];

        for (int t = 1; t <= k; t++) {
            long bestBuy = -prices[0];   // normal buy
            long bestSell = prices[0];   // short sell

            curr[0] = 0;

            for (int i = 1; i < n; i++) {
                // Update dp
                curr[i] = Math.max(curr[i - 1],
                        Math.max(prices[i] + bestBuy,
                                 bestSell - prices[i]));

                // Update best states
                bestBuy = Math.max(bestBuy, prev[i - 1] - prices[i]);
                bestSell = Math.max(bestSell, prev[i - 1] + prices[i]);
            }

            // Move current to previous
            long[] temp = prev;
            prev = curr;
            curr = temp;
        }

        return prev[n - 1];
    }
}
