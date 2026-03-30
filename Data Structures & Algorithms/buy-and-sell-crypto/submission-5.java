class Solution {
    public int maxProfit(int[] prices) {
        int left =0, right = 1;
        int maxP=0;

        while(right < prices.length){
            if(prices[left] < prices[right]){
                int profit = prices[right] - prices[left];
                maxP = Math.max(maxP, profit);
            } 
            // If prices[left] is bigger than prices[right] index right become left and iterate from that;
            else {
                left = right;
            }

            right++;
        }

        return maxP;
    }
}
