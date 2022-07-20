# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        nodeLeft = ListNode()
        nodeRight = ListNode()
        resultNode = nodeLeft
        rightStart = nodeRight
        while head:
            if(head.val<x):
                nodeLeft.next = head
                nodeLeft = nodeLeft.next
            else:
                nodeRight.next = head
                nodeRight = nodeRight.next
            head = head.next
        
        nodeRight.next = None
        # print(nodeLeft)
        # print(nodeRight)
        nodeLeft.next = rightStart.next
        return resultNode.next
                
        