class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if(n==0){
            return;
        }
        int num1_len = m-1;
        int num2_len = n-1;
        int total_len = m+n-1;
        while(num1_len>=0&&num2_len>=0){
            if(nums2[num2_len]>nums1[num1_len]){
                nums1[total_len] = nums2[num2_len];
                num2_len--;
                total_len--;
            }else{
                nums1[total_len] = nums1[num1_len];
                nums1[num1_len] = nums2[num2_len];
                num1_len--;
                total_len--;
            }
        }
        while(num2_len>=0){
            nums1[total_len] = nums2[num2_len];
            num2_len--;
            total_len--;
        }
        
    }
}