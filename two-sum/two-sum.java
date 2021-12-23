class Solution {
    
    HashMap<Integer, Integer> map = new HashMap<>();
    
    public int[] twoSum(int[] nums, int target) {
        for(int i=0;i<nums.length;i++){
            if(map.containsKey(target-nums[i])&&map.get(target-nums[i])!=i){
                return new int[]{i, map.get(target-nums[i])};
            }
            map.put(nums[i],i);
        }
        return new int[]{};
    }
}