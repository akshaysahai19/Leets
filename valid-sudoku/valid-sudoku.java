class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashMap<String,Integer> map_row = new HashMap<String,Integer>();
        HashMap<String,Integer> map_col = new HashMap<String,Integer>();
        HashMap<String,Integer> map_box = new HashMap<String,Integer>();
        int rowCount = 9;
        int colCount = 9;
        for(int i=0;i<9;i++){//rows
            for(int j=0;j<9;j++){//columns
                int box = ((i/3) *3+j/3);
                if(board[i][j]!='.'){
                    if(map_row.containsKey(
                        board[i][j]+""+i)||
                       map_col.containsKey(board[i][j]+""+j)||
                        map_box.containsKey(board[i][j]+""+box)){
                        // map_row.containsKey(board[i][j]+""+i+j+box)
                        return false;
                }else{
                    map_row.put(board[i][j]+""+i,1);
                    map_col.put(board[i][j]+""+j,1);
                    map_box.put(board[i][j]+""+box,1);
                    // map_row.put(board[i][j]+""+i+j+box,1);
                    }
                }
            }
        }
        
        return true;
    }
}