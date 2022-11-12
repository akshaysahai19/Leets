class MedianFinder:

    def __init__(self):
        self.stream = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.stream, num)
        

    def findMedian(self) -> float:
        mid = len(self.stream)//2
        self.stream.sort()
        if len(self.stream)%2==0:
            return (self.stream[mid-1]+self.stream[mid])/2
        else:
            return self.stream[mid]
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()