# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists)==1:
            return lists[0]
        
        if not lists:
            return None
        
        def mergeTwoSorted(aList,bList):
            dummy = ListNode(-1)
            resultList = dummy
            
            while aList!=None and bList!=None:
                if aList.val<bList.val:
                    dummy.next = aList
                    aList = aList.next
                else:
                    dummy.next = bList
                    bList = bList.next
                dummy = dummy.next
            
            if aList!=None:
                dummy.next = aList
                
            if bList!=None:
                dummy.next = bList
            
            return resultList.next
        
        result = None
        if len(lists) >= 2:
            result = mergeTwoSorted(lists[0],lists[1])
        
        for i, li in enumerate(lists[2:]):
            result = mergeTwoSorted(result, li)
        
        return result
                
                    
                    
                
        