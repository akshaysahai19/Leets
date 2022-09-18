# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        odd = head
        evenHead = ListNode()
        even = evenHead
        k = 1
        while head!=None:
            if k%2!=0:
                evenHead.next = head.next
                evenHead = evenHead.next
                if head.next!= None:
                    head.next = head.next.next
                    head = head.next
                else:
                    head = None
                k+=1
            else:
                head = head.next
            k+=1
        
        result = ListNode()
        result.next = odd
        while odd.next:
            odd = odd.next
        odd.next = even.next

        return result.next
            
        