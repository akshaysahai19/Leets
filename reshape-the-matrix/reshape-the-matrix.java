class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int original_rows = mat.length;
        int original_col = mat[0].length;
        int[][] new_mat = new int[r][c];
        int current_row = 0;
        int current_col = 0;
        if(r*c!=original_rows*original_col){
            return mat;
        }
        for(int i = 0; i<original_rows;i++){
            for(int j=0;j<mat[i].length;j++){
                new_mat[current_row][current_col] = mat[i][j];
                if(current_col==c-1&&current_row<=r-1){
                    current_row++;
                    current_col = 0;
                }else{
                    current_col++;
                }
            }
        }
        return new_mat;
    }
}