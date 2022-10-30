class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        indices = sorted(range(len(growTime)), key=lambda x: -growTime[x]) 

        startTime = 0
        currTime = 0
        for i in indices:
            currTime+=plantTime[i]
            startTime = max(startTime, currTime+growTime[i])
        return startTime
        
        