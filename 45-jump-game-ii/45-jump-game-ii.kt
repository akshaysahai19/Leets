class Solution {
    fun jump(nums: IntArray): Int {
        var currentMaxReach = 0
        var lastMaxReach = 0
        var jumpCounts = 0
        
        if(nums.size==1){
            return 0
        }
        
        for(n in 0..nums.size-1){
            
            
            if(nums[n]+n>=currentMaxReach){
                currentMaxReach = nums[n]+n 
            }
            
            if(lastMaxReach==0 && nums[n]+n>lastMaxReach){
                lastMaxReach = nums[n]+n
                // currentMaxReach = nums[n]+n
                jumpCounts++;
            }else if(n>=lastMaxReach){
                lastMaxReach = currentMaxReach
                jumpCounts++;    
            }
            
            
            if(lastMaxReach>=nums.size-1){
                return jumpCounts
            }
            
        }    
        return 0
    }
}