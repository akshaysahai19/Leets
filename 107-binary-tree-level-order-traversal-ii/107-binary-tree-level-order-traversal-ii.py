# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
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
            
        return list(hashMap.values())[::-1]    