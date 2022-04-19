class Solution {
    
    val mem = mutableMapOf<Int, Int>()
    
    fun rob(nums: IntArray): Int {
        return maxOf(maxRob(nums, 0), maxRob(nums, 1))
    }
    
    fun maxRob(nums:IntArray, n:Int):Int{
        
        if(mem[n]!=null){
            return mem[n] as Int
        }
        
        if(n>nums.size-1){
            return 0
        }
        for(i in n+2..nums.size){
            
            mem[n]=(nums[n]+maxOf(maxRob(nums, i), maxRob(nums, i+1))) as Int
            return mem[n] as Int
        }
        
        if(mem[n]==null){
            mem[n] = nums[n]
        }
        
        return mem[n] as Int
    }
    
}