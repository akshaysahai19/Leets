class Solution {
    public int search(int[] nums, int target) {
        return getItem(nums,0,nums.length-1,target);
    }
    
    public int getItem(int[] nums, int left, int right, int target){
        int mid = Math.floorDiv((right+left),2);
        if(left>right){
            return -1;
        }
        if(nums[mid]==target){
            return mid;
        }else{
            if(nums[mid]>target){
                return getItem(nums, left, mid-1, target);
            }else{
                return getItem(nums, mid+1, right, target);
            }
        }
    }
}