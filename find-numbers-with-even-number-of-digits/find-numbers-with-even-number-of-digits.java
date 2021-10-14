class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        for(int i=0;i<nums.length;i++){
            int digits = 0;
            int number = nums[i];
            int localCounts=0;
            while(number>0){
                localCounts +=1;
                number=number/10;
            }
            if(localCounts%2==0){
                count+=1;
            }
        }
        return count;
    }
}