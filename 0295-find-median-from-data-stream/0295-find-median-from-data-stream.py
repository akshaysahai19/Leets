import bisect

class MedianFinder:

    def __init__(self):
        self.stream = []
        

    def addNum(self, num: int) -> None:
        index = bisect.bisect_left(self.stream, num)
        self.stream.insert(index, num)

    def findMedian(self) -> float:
        mid = len(self.stream)//2
        if len(self.stream)%2==0:
            return (self.stream[mid-1]+self.stream[mid])/2
        else:
            return self.stream[mid]
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()