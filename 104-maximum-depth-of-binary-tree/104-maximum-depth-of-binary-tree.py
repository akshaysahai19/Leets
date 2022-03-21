# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        hashMap = {}
        
        def recursiveLevelOrder(root, index):
            if not root:
                return
            
            if index in hashMap:
                hashMap[index].append(root.val)
            else:
                hashMap[index] = [root.val]
            
            recursiveLevelOrder(root.left, index+1)
            recursiveLevelOrder(root.right, index+1)
            
            return
        
        recursiveLevelOrder(root, 0)
        if len(hashMap.keys())>0:
            return max(hashMap.keys())+1
        else:
            return 0