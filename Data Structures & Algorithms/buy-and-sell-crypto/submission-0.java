class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        for(int i=0; i<prices.length-1; i++){
            for(int j=i; j<prices.length; j++){
                int temp = prices[j]-prices[i];
                if(temp > profit){
                    profit = temp;
                }
            }
        }

        return profit;
    }
}
