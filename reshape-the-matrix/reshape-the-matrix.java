class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int original_row = mat.length;
        int original_col = mat[0].length;
        int[][] new_mat = new int[r][c];
        if(c*r!=original_col*original_row){
            return mat;
        }
        int x = 0;
        int y = 0;
        for(int i = 0;i<original_row;i++){
            for(int j=0;j<original_col;j++){
                new_mat[x][y]=mat[i][j];
                if(y==c-1&&x<r){
                    x++;
                    y=0;
                }else{
                    y++;
                }
            }
        }
        return new_mat;
    }
}