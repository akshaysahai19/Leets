# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        hashMap = {}
        
        def findLevelOrder(root, index):
            
            if not root:
                return None
            
            if index in hashMap:
                hashMap[index].append(root.val)
            else:
                hashMap[index] = [root.val]
            
            findLevelOrder(root.left, index+1)
            findLevelOrder(root.right, index+1)
        
        findLevelOrder(root, 0)
        
        return hashMap.values()
        