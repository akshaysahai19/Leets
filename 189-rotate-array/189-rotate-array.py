class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(k):
        #     nums[i] = reverse[i:len(nums)-1-i][-1]
        k%=len(nums)
        z = nums[len(nums)-k:len(nums)] + nums[:len(nums)-k]
        print(z)
        # for j in range(len(nums)-1,-1,-1):
        #     nums[j]=nums[j-1]
        # nums[0]=temp   
        # print(nums)
        nums[::] = z