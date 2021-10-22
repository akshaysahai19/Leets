class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        for(int row = 0;row<matrix.length;row++){
            if((matrix[row][0]<target||matrix[row][0]==target)&&(matrix[row][matrix[row].length-1]==target||matrix[row][matrix[row].length-1]>target)){
                for(int j=0;j<matrix[row].length;j++){
                    if(matrix[row][j]==target){
                        return true;
                    }
                }
            }else{
                continue;
            }
        }
        return false;
    }
}