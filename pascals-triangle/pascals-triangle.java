class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> mat = new ArrayList<List<Integer>>();
        ArrayList<Integer> inside = new ArrayList<Integer>();
        for(int i=0;i<numRows;i++){
            inside = new ArrayList<Integer>();
            for(int j=0;j<=i;j++){
                if(j==0||j==i){
                    inside.add(j,1);
                }else{
                    inside.add(j,mat.get(i-1).get(j)+mat.get(i-1).get(j-1));
                }
            }
            mat.add(i,inside);
        }
        return mat;
    }
}