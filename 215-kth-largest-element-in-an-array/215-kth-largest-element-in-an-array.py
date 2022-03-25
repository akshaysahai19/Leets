class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        largest = 0
        
        # if k==1:
        #     return nums[0]
        
        mapped ={}
        
        return nums[len(nums)-k]
        
        # for i in range(len(nums)-1, 0, -1):
        #     # if nums[i] not in mapped:
        #     #     largest+=1
        #     #     mapped[nums[i]] = True
        #     # if largest==k:
        #     #     return nums[i]
        #     return nums[]
               
        return nums[len(nums)-1]
        