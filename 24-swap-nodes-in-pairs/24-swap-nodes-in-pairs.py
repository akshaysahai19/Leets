# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        resultNode = ListNode()
        prev = ListNode()
        prev.next = head
        resultNode.next = prev
        
        while head and head.next:
            temp = head.next
            head.next = temp.next
            temp.next = head
            prev.next = temp
            head = head.next
            prev = temp.next
        
        return resultNode.next.next