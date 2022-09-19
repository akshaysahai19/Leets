# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        sums = []
        currSum = 0
        
        while head:
            if head.val!=0:
                currSum+=head.val
            else:
                if currSum!=0:
                    sums.append(currSum)
                    currSum = 0
            head = head.next
        if currSum!=0:
            sums.append(currSum)
        
        tempHead = ListNode()
        tempList = ListNode()
        tempList.next = tempHead
        
        for n in sums:
            tempHead.next = ListNode(n)
            tempHead = tempHead.next
        
        return tempList.next.next
        