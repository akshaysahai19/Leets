class Solution {
    public int removeDuplicates(int[] nums) {
        int x=0;
        int y=0;
        int count=0;
        while(x<=y && y<nums.length){
            if(nums[x]==nums[y]){
                count++;
                if(count==2){
                    nums[++x]=nums[y];
                }
                y++;
            }else{
                nums[++x]=nums[y];
                count = 1;
                y++;
            }
        }
        return ++x;
    }
}