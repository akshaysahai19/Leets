# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        countNode = head
        while countNode:
            countNode = countNode.next
            length+=1
        
        currPos = 0
        dummy = ListNode()
        dummy.next = head
        resultNode = dummy
        while dummy:
            if currPos==length-n:
                dummy.next = dummy.next.next
                break
            dummy = dummy.next
            currPos+=1
        return resultNode.next
                
        