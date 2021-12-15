class Solution {
    public int removeDuplicates(int[] nums) {
        int slow=0;
        int fast = 1;
        while(slow<fast&&fast<nums.length){
            if(nums[slow]!=nums[fast]){
                slow++;
                nums[slow]=nums[fast];
                fast++;
            }else{
                fast++;
            }
        }
        return slow+1;
    }
}