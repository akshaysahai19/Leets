class StockPrice:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        self.timeStampMap = {}
        self.maxTimeStamp = 0
        

    def update(self, timestamp: int, price: int) -> None:
        
        self.timeStampMap[timestamp] = price 
        self.maxTimeStamp = max(self.maxTimeStamp, timestamp)
            
        heapq.heappush(self.minHeap, (price, timestamp))
        heapq.heappush(self.maxHeap, (-price, timestamp))

    def current(self) -> int:
        return self.timeStampMap[self.maxTimeStamp]
        

    def maximum(self) -> int:
        price, timestamp = self.maxHeap[0]
        while -price!=self.timeStampMap[timestamp]:
            heapq.heappop(self.maxHeap)
            price, timestamp = self.maxHeap[0]
        return -price

    def minimum(self) -> int:
        price, timestamp = self.minHeap[0]
        while price!=self.timeStampMap[timestamp]:
            heapq.heappop(self.minHeap)
            price, timestamp = self.minHeap[0]
        return price
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()