class Solution {
    
    public boolean canJump(int[] nums) {
        int maxCheck = nums.length-1;
        for(int i=nums.length-2;i>=0;i--){
            if(nums[i]+i>=maxCheck){
                maxCheck = i;    
            }
        }
        return maxCheck==0;
    }
}