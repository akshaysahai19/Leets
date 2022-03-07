class Solution {
    
    HashMap<Integer,Integer> map = new HashMap<>();
    
    public int rob(int[] nums) {
        if(nums.length==1){
            return nums[0];
        }
        return Math.max(houseRob(nums, 0),houseRob(nums, 1));
    }
    
    public int houseRob(int[] nums, int index){
        if(map.containsKey(index)){
            return map.get(index);
        }
        if(index>nums.length-1){
            return 0;
        }
        map.put(index,nums[index]+ Math.max(houseRob(nums, index+2),houseRob(nums, index+3)));
        return map.get(index);
    }
}