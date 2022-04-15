class Solution {
    
    HashMap<Integer,Integer> dp = new HashMap<Integer, Integer>();
    
    public int climbStairs(int n) {
        return climbStairsCount(n);    
    }
    
    public int climbStairsCount(int n){
        
        if(dp.containsKey(n)){
            return dp.get(n);
        }
        
        if(n==0){
            return 1;
        }
        if(n>=2){
            dp.put(n, climbStairsCount(n-1)+climbStairsCount(n-2));
            return dp.get(n);
        }else if(n==1){
            dp.put(n, climbStairsCount(n-1));
            return dp.get(n);
        }
        return 0;
    }
    
}