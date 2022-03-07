class Solution {
    
    HashMap<String,Integer> map = new HashMap<>();

    
    public int rob(int[] nums) {
        if(nums.length==1){
            return nums[0];
        }
        
        int currentMax = 0;
        for(int i=0;i<nums.length;i++){
            int val = houseRob(nums, i, i);
            if(val>currentMax){
                currentMax = val;
            }
        }
        return currentMax;
    }
    
    public int houseRob(int[] nums, int index, int startIndex){
        if(map.containsKey(index+"_"+startIndex)){
            return map.get(index+"_"+startIndex);
        }
        
        if(startIndex==0 && index==nums.length-1){
            return 0;
        }
        
        if(index>nums.length-1){
            return 0;
        }
        
        map.put(index+"_"+startIndex,nums[index]+ Math.max(houseRob(nums, index+2, startIndex),houseRob(nums, index+3, startIndex)));
        
        return map.get(index+"_"+startIndex);
    }
}