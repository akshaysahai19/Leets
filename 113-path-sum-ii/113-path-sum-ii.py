# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        result = []
        
        def findSumPairs(node, currPairs, currSum):
            
            if not node:
                return []
            
            if not node.left and not node.right and currSum==node.val:
                result.append(currPairs+[node.val])
                return
            
            a = findSumPairs(node.left, currPairs+[node.val], currSum-node.val)
            b = findSumPairs(node.right, currPairs+[node.val], currSum-node.val)
            
        findSumPairs(root, [], targetSum)
        
        return result
            
            