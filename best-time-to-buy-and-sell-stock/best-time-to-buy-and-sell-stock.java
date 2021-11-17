class Solution {
    public int maxProfit(int[] prices) {
        int output = 0;
        int min = Integer.MAX_VALUE;
        for(int i=0;i<prices.length;i++){
            if(prices[i]<min){
                min=prices[i];
            }
            if(prices[i]-min>output){
                output = prices[i]-min;
            }
        }
        return output;
    }
}