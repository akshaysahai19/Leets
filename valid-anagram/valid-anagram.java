class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character,Integer> s_map = new HashMap<Character,Integer>();
        if(s.length()!=t.length()){
            return false;
        }
        for(int i=0;i<s.length();i++){
            if(s_map.containsKey(s.charAt(i))){
                s_map.put(s.charAt(i),s_map.get(s.charAt(i))+1);
            }else{
                s_map.put(s.charAt(i),1);
            }
        }
        
        for(int i=0;i<t.length();i++){
            if(!s_map.containsKey(t.charAt(i))){
                return false;
            }
            if(s_map.containsKey(t.charAt(i))){
                s_map.put(t.charAt(i),s_map.get(t.charAt(i))-1);
            }
        }
        System.out.println(s_map);
        for(int i=0;i<s.length();i++){
           if(s_map.containsKey(s.charAt(i))&&s_map.get(s.charAt(i))==0){
               continue;
           }else{
               return false;
           } 
        }
        
    return true;
    }
    

}