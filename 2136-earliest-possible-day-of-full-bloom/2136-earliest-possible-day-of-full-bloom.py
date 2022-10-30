class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        times = sorted(zip(growTime, plantTime))

        bloomingTime = 0
        for grow, plant in times:
            bloomingTime = max(bloomingTime, grow)+plant
        return bloomingTime
        
        