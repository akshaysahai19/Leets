class Solution {
    int res = Integer.MAX_VALUE;
    public int findMin(int[] nums) {
        if (nums.length == 1) {
            res = Math.min(res, nums[0]);
            return res;
        }
        
        int mid = nums.length/2;
        findMin(Arrays.copyOfRange(nums, 0, mid));
        findMin(Arrays.copyOfRange(nums, mid, nums.length));
        
        return res;
    }
}