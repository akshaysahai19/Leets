class Solution {
    
    val mem = mutableMapOf<String, Int>()
    
    fun rob(nums: IntArray): Int {
        if(nums.size==1){
            return nums[0]
        }
        var maxRobberyAmount = 0
        for(i in 0..nums.size){
            maxRobberyAmount = maxOf(maxRobberyAmount, maxRob(nums, i, i))
        }
        return maxRobberyAmount
    }
    
    fun maxRob(nums: IntArray, current:Int, start:Int):Int{
        var currentPos = current.toString() + "-" + start.toString()
        if(mem[currentPos]!=null){
            return mem[currentPos] as Int
        }
        
        if(current>nums.size-1){
            return 0
        }
        if(current==nums.size-1){
            if(start==0){
                return 0
            }
        }
            mem[currentPos] = nums[current]+maxOf(maxRob(nums, current+2, start), maxRob(nums, current+3, start))
            return mem[currentPos] as Int
        
        
    }
}