class Solution {
    
    HashMap<Integer,Integer> dp = new HashMap<>();
    
    public int tribonacci(int n) {
        
        if(dp.containsKey(n)){
            return dp.get(n);
        }
        
        if(n==0){
            return 0;
        }    
        if(n==1||n==2){
            return 1;
        }
        dp.put(n,tribonacci(n-3)+tribonacci(n-2)+tribonacci(n-1));
        return dp.get(n);
    }
}