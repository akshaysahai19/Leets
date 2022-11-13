class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        n = len(bottoms)
        
        def rotate(x):
            rot_a = rot_b = 0
            
            for i in range(n):
                if tops[i]!=x and bottoms[i]!=x:
                    return -1
                elif tops[i]!=x:
                    rot_a+=1
                elif bottoms[i]!=x:
                    rot_b+=1
            
            return min(rot_a, rot_b)
        
        rotations_top = rotate(tops[0])
        rotations_bottom = rotate(bottoms[0])
        
        if rotations_top!=-1 and rotations_bottom!=-1:
            return min(rotations_top, rotations_bottom)
        
        if rotations_top!=-1:
            return rotations_top
        
        if rotations_bottom!=-1:
            return rotations_bottom
        
        return -1
        
        