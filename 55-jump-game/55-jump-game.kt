class Solution {
    
    val mem = mutableMapOf<Int, Boolean>();
    
    fun canJump(nums: IntArray): Boolean {
        var maxReach = 0
        for(n in 0..nums.size-1){
            // println(nums[n]+n)
            if(nums[n]+n>maxReach){
                maxReach = nums[n]+n    
            }
            
            if(maxReach>=nums.size-1){
                return true
            }
            
            if(maxReach==n && nums[n]==0){
                return false
            }
        }  
        return false
    }
    
}