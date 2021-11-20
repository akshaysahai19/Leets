class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int[][] mem = new int[text1.length()][text2.length()];
        return getBestMatch(text1, text2, mem);
    }
    
    public int getBestMatch(String text1, String text2, int[][] mem) {
        if(text1.length()==0||text2.length()==0){
            return 0;
        }
        
        if(mem[text1.length()-1][text2.length()-1]!=0){
            System.out.println("Mem - "+mem[text1.length()-1][text2.length()-1]);
            return mem[text1.length()-1][text2.length()-1];
        }
        
        if(text1.charAt(text1.length()-1)==text2.charAt(text2.length()-1)){
            mem[text1.length()-1][text2.length()-1] = 1 + getBestMatch(text1.substring(0,text1.length()-1), text2.substring(0,text2.length()-1),mem);
            return mem[text1.length()-1][text2.length()-1];
        }else{
            mem[text1.length()-1][text2.length()-1] = max(getBestMatch(text1.substring(0,text1.length()-1), text2, mem),getBestMatch(text1, text2.substring(0,text2.length()-1),mem));
            
            return mem[text1.length()-1][text2.length()-1];
        }
    }
    
    public int max(int x, int y){
        return x>y?x:y;
    }
}