# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        node = ListNode()
        node.next = head
        while head.next:
            temp = head.next
            head.next = temp.next
            temp.next = node.next
            node.next = temp
        
        return node.next
            
        