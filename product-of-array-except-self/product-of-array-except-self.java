class Solution {
    public int[] productExceptSelf(int[] nums) {
        int leftMultiplication = 1;
        int rightMultiplication = 1;
        int[] leftMul = new int[nums.length];
        int[] rightMul = new int[nums.length];
        int[] formedMul = new int[nums.length];
        for(int i=0;i<nums.length;i++){
            leftMultiplication = leftMultiplication*nums[i];
            leftMul[i] = leftMultiplication;
        }
        for(int i=nums.length-1;i>=0;i--){
            rightMultiplication = rightMultiplication*nums[i];
            rightMul[i] = rightMultiplication;
        }
        
        for(int i=0;i<=nums.length-1;i++){
            if(i==0){
                formedMul[i] = rightMul[i+1];
            }else if(i==nums.length-1){
                formedMul[i] = leftMul[i-1];
            }else{
               formedMul[i] = leftMul[i-1]*rightMul[i+1];                
            }
        }
        return formedMul;
    }
}