class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
    if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
        return false;
    }
    int row = 0;
    int col = matrix[0].length - 1;
    while (row < matrix.length && col >= 0) {
        if (matrix[row][col] == target) {
            return true;
        } else if (matrix[row][col] < target) {
            row++;
        } else {
            col--;
        }
    }
    return false;
}
    
    
    // public boolean searchMatrix(int[][] matrix, int target) {
    //     for(int row = 0;row<matrix.length;row++){
    //         if((matrix[row][0]<target||matrix[row][0]==target)&&(matrix[row][matrix[row].length-1]==target||matrix[row][matrix[row].length-1]>target)){
    //             for(int j=0;j<matrix[row].length;j++){
    //                 if(matrix[row][j]==target){
    //                     return true;
    //                 }
    //             }
    //         }else{
    //             continue;
    //         }
    //     }
    //     return false;
    // }
    
}