# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        currSum = 0
        
        tempHead = ListNode()
        resultHead = tempHead
        
        while head:
            if head.val!=0:
                currSum+=head.val
            else:
                if currSum!=0:
                    tempHead.next = ListNode(currSum)
                    tempHead = tempHead.next
                    currSum = 0
            head = head.next
        
        return resultHead.next
        