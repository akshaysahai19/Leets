class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        def reverse(start, end, n):
            while start<end:
                tempEnd = nums[end]
                nums[end] = nums[start]
                nums[start] = tempEnd
                start+=1
                end-=1
        
        reverse(0, n-1, nums)
        reverse(0, k-1, nums)
        reverse(k, n-1, nums)
        