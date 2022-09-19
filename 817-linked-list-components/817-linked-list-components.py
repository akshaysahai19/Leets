# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        
        pairs = []
        while head!=None:
            if head.val in nums:
                pairs.append(head.val)
            else:
                pairs.append(-1)
            head = head.next
            
        count = 0
        for i in range(len(pairs)-1):
            if pairs[i]!=-1:
                if pairs[i+1]==-1:
                    count+=1
        if pairs[-1]!=-1:
            count+=1
            
        return count
            
                    
            
        