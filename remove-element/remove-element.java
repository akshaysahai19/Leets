class Solution {
    public int removeElement(int[] nums, int val) {
        int x=0;
        if(nums.length==0){
            return x;
        }
        int y=nums.length-1;
        while(x<=y){
            if(nums[x]==val){ 
                nums[x]=nums[y];
                y--;
            }else{
                x++;
            }
        }
        return x;
    }
}