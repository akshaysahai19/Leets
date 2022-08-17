class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distanceList = []
        
        for point in points:
            distance = (point[0]*point[0] + point[1]*point[1])**0.5
            distanceList.append([distance, point])
        
        distanceList = sorted(distanceList)
        
        result = []
        for item in distanceList:
            result.append(list(item[1]))
        
        return result[:k]
        