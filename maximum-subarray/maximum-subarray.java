class Solution {
    public int maxSubArray(int[] nums) {
        int max_sum = nums[0];
        int current_sum = 0;
        for(int i=0;i<nums.length;i++){
            if(current_sum+nums[i]>nums[i]){
                current_sum = current_sum+nums[i];
            }else{
                current_sum = nums[i];
            }
            if(current_sum>max_sum){
                max_sum=current_sum;
            }
            // System.out.println("Current - "+current_sum);
            // System.out.println("Max - "+ max_sum);
        }
        return max_sum;
    }
}

// https://www.youtube.com/watch?v=2MmGzdiKR9Y