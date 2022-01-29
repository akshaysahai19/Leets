class Solution {

    HashMap<Integer,Integer> mem = new HashMap<>();
    
    public int climbStairs(int n) {
        return climbingStairsNew(n,mem);
    }
    
    public int climbingStairsNew(int n, HashMap<Integer,Integer> mem){
        if(n<=0){
            mem.put(n,0);
            return mem.get(n);
        }
        if(n==1){
            mem.put(1,1);
            return mem.get(n);
        }
        if(n==2){
            mem.put(2,2);
            return mem.get(n);
        }
        if(!mem.containsKey(n)){
            mem.put(n,climbingStairsNew(n-1,mem)+climbingStairsNew(n-2,mem));
        }
        return mem.get(n);
    }
}