class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character,Integer> map = new HashMap<Character,Integer>();
        for(int i=0;i<s.length();i++){
            System.out.println(s.charAt(i));
            if(map.containsKey(s.charAt(i))){
                map.put(s.charAt(i),map.get(s.charAt(i))+1);
            }else{
                map.put(s.charAt(i),1);
            }
        }
        
        for(int i=0;i<s.length();i++){
            System.out.println(s.charAt(i));
            if(map.get(s.charAt(i))==1){
                return i;
            }
        }
        return -1;
    }
}