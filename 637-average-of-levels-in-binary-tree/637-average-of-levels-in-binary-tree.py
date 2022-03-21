# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
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
        
        averages = []
        for item in hashMap.values():
            averages.append((sum(item)/len(item)))    
        
        return averages
        