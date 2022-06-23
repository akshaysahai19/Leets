class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        for i,x in enumerate(nums):
            target=0-x
            d_map = {}
            for j,y in enumerate(nums[i+1:]):
                if target-y in d_map:
                    val = [x,target-y, y]
                    val.sort()
                    if val not in output:
                        output.append(val)
                else:
                    d_map[y]=j
    
        finalOutput = []
        # for y in output:
        #     if y not in finalOutput:
        #         finalOutput.append(y)
        return output
                    
            
        
        