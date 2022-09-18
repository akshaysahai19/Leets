# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return None
        
        temp = head
        count = 0
        while temp:
            temp = temp.next
            count+=1
            
        def splitPart(headNode, shift):
            
            k=1
            left = ListNode()
            tempLeft = headNode
            left.next = tempLeft
            while k<count-shift:
                tempLeft = tempLeft.next
                k+=1
            right = tempLeft.next
            tempLeft.next = None
                
            return left.next, right
        
        
        left, right = splitPart(head, k%count)
        result = ListNode()
        result.next = right
        
        if not right:
            return left 
        
        while right.next:
            right = right.next
        right.next = left
        
        return result.next
                