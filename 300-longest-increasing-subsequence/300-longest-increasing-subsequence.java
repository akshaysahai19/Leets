class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] mins = new int[nums.length];
        for(int i=0;i<nums.length;i++){
            for(int j=0;j<i;j++){
                if(nums[i]>nums[j]){
                    if(mins[i]>mins[j]){
                        mins[i] = mins[i];
                    }else{
                        mins[i] = 1 + mins[j];
                    }
                }
            }
        }
        
        int max = 0;
        for(int x=0;x<nums.length;x++){
            if(max<mins[x]){
                max = mins[x];
            }
            
        }
        return max+1;
        
    }
    
}