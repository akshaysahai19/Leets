# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        cameras = 0
        
        def countCameras(node):
            
            nonlocal cameras
            
            if not node:
                return 1
            
            left = countCameras(node.left)
            right = countCameras(node.right)
            
            # 1 is monitored
            # 2 is unmonitored
            # 3 is has camera
            if left==1 and right==1:
                return 2    #unmonitored
            
            if left==2 or right==2:
                cameras+=1
                return 3    #has camera
            
            if left==3 or right==3:
                return 1    #onitored
            
            return 1
        
        count = countCameras(root)

        if count==2:
            cameras+=1;
        
        return 1 if cameras==0 else cameras
            