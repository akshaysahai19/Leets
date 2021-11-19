class Solution {
    public int searchInsert(int[] nums, int target) {
        return findPos(nums,target,0,nums.length-1,-1);
    }
    
    public int findPos(int[] nums, int target, int left, int right, int fit_position){
        int mid = left+(right-left)/2;
        if(left>right){
            System.out.println("value fit - "+fit_position);
            return fit_position;
        }
        if(nums[mid]==target){
            System.out.println("value mid - "+fit_position);
            return mid;
        }
        if(nums[mid]>target){
            fit_position=mid;
            System.out.println("value mid>target - "+fit_position);
            return findPos(nums,target,left,mid-1,fit_position);
        }else{
            System.out.println("value mid<=target - "+fit_position);
            fit_position=mid+1;
            return findPos(nums,target,mid+1,right,fit_position);
        }
    }
}