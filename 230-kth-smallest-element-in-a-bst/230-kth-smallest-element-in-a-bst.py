# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        rootList = []
        
        def findInOrder(root):
            if not root:
                return 
            
            findInOrder(root.left)
            rootList.append(root.val)
            findInOrder(root.right)
        
    
#         def findPreOrder(root):
#             if not root:
#                 return 

#             rootList.append(root.val)
#             findPreOrder(root.left)
#             findPreOrder(root.right)
        
    
        findInOrder(root)
        print(rootList)
        # findPreOrder(root)
        # print(rootList)
        heapq.heapify(rootList)
        while k>1:
            heapq.heappop(rootList)
            k-=1
        
        return heapq.heappop(rootList)
        