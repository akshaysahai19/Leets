class Solution {
    
    int val = -1;
    
    public int search(int[] nums, int target) {
        return searchArray(nums,target,0);
    }
    
    public int searchArray(int[] nums, int target, int append){
        int mid = nums.length/2;
        if(nums[mid]==target){
            val = append+mid;
            return append+mid;
        }
        if(mid>0){
            searchArray(Arrays.copyOfRange(nums, 0, mid),target, append); 
            searchArray(Arrays.copyOfRange(nums, mid, nums.length),target,append+mid);
        }
        return val;
    }
    
}