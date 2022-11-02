class MyCalendar:

    def __init__(self):
        self.meetings = []
        

    def book(self, start: int, end: int) -> bool:
        self.meetings.sort()
        meet = (start, end)
        for pair in self.meetings:
            if meet[0]<pair[1] and meet[1]>pair[0]:
                return False
        self.meetings.append((start, end))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)