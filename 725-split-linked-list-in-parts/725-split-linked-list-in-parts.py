# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        tempCount = head
        count = 0
        while tempCount:
            tempCount = tempCount.next
            count+=1
        
        def partition(count, n):
            pairs = []
            k, m = divmod(count, n)
            for i in range(n):
                start = i * k + min(i, m)
                end = start + k + (i < m)
                pairs.append(end-start)
            return pairs
        
        pairs = partition(count, k)
        result = []
        
        for n in pairs:
            temp = head
            tempPairHead = ListNode()
            tempPairHead.next = temp
            k = 1
            while head:
                if k==n:
                    head = head.next
                    temp.next = None
                    break
                head = head.next
                temp = temp.next
                k+=1
            result.append(tempPairHead.next)
            
        return result
        
        