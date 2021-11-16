class Solution {
    public void moveZeroes(int[] nums) {
        int x=0;
        int y=1;
        while(x<=y&&y<nums.length){
            if(nums[x]==0){
                if(nums[y]==0){
                    y++;
                }else{
                    nums[x]=nums[y];
                    nums[y]=0;
                    y++;
                    x++;
                }
            }else{
                x++;
                y++;
            }    
        }
    }
}