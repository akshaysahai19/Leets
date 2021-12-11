class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[i].length;j++){
                if(grid[i][j]=='1'){
                    count++;
                    landFollowing(grid,i,j);
                }
            }
        }
        return count;
    }
    
    public void landFollowing(char[][] grid, int i, int j){
        if(grid[i][j]=='0'){
            return;
        }else{
            grid[i][j] = '0';
        }
        
        if(i-1>=0){
            if(grid[i-1][j]=='1'){
                landFollowing(grid, i-1,j);
            }
        }
        if(i+1<=grid.length-1){
            if( grid[i+1][j]=='1'){
                landFollowing(grid, i+1,j);
            }
        }
        if(j-1>=0){
            if(grid[i][j-1]=='1'){
                landFollowing(grid, i,j-1);
            }
        }
        if(j+1<=grid[i].length-1){
            if( grid[i][j+1]=='1'){
                landFollowing(grid, i,j+1);
            }
        }
    }
}