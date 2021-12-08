class Solution {
    public int maxArea(int[] height) {
        if(height.length==2){
            return Math.min(height[0],height[1]);
        }
        int x =0;
        int y=height.length-1;
        int currentMax = 0;
        int localArea = 0;
        while(x<=y){
            localArea = (y-x)*(Math.min(height[x],height[y]));
            if(height[x]>height[y]){
                y--;
            }else{
                x++;
            }
            
            if(localArea>currentMax){
                currentMax = localArea;
            }
        }
        return currentMax;
    }
}