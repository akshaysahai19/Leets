# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        rootList = []
        
        def findInOrder(root):
            if not root:
                return 
            
            findInOrder(root.left)
            rootList.append(root.val)
            findInOrder(root.right)
        
        findInOrder(root)
        rootList = list(set(rootList))
        heapq.heapify(rootList)
        
        
        print(rootList)
        k = 2
        
        
        if len(rootList)<k:
            return -1
        
        while k>1:
            heapq.heappop(rootList)
            k-=1
        
        return heapq.heappop(rootList)