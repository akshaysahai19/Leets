class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        diffs = [abs(plantTime[i]-growTime[i]) for i in range(len(plantTime))]

        indices = sorted(range(len(plantTime)), key=lambda x: -growTime[x]) 

        startTime = 0
        currTime = 0
        for i in indices:
            currTime+=plantTime[i]
            startTime = max(startTime, currTime+growTime[i])
        return startTime
        
        