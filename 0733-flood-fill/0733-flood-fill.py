class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        def fillColor(i,j, c):
            
            if i<0 or i>=m or j<0 or j>=n or image[i][j]!=c:
                return
            if image[i][j]!=color:
                image[i][j] = color
                fillColor(i+1,j,c)
                fillColor(i-1,j,c)
                fillColor(i,j+1,c)
                fillColor(i,j-1,c)
        
        fillColor(sr,sc, image[sr][sc])
        
        return image