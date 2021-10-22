class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character,Integer> ransomNote_map = new HashMap<Character,Integer>();
        HashMap<Character,Integer> magazine_map = new HashMap<Character,Integer>();
        for(int i=0;i<magazine.length();i++){
            if(magazine_map.containsKey(magazine.charAt(i))){
                magazine_map.put(magazine.charAt(i),magazine_map.get(magazine.charAt(i))+1);
            }else{
                magazine_map.put(magazine.charAt(i),1);
            }
        }
        
        for(int i=0;i<ransomNote.length();i++){
            if(magazine_map.containsKey(ransomNote.charAt(i))){
                if(ransomNote_map.containsKey(ransomNote.charAt(i))){
        ransomNote_map.put(ransomNote.charAt(i),ransomNote_map.get(ransomNote.charAt(i))+1);
                }else{
                    ransomNote_map.put(ransomNote.charAt(i),1);
                }
            }else{
                return false;
            }
        }
        System.out.println(ransomNote_map);
        System.out.println(magazine_map);
        for(int i=0;i<ransomNote.length();i++){
           if(magazine_map.containsKey(ransomNote.charAt(i))){
               if(ransomNote_map.containsKey(ransomNote.charAt(i))){
                  if(ransomNote_map.get(ransomNote.charAt(i))>magazine_map.get(ransomNote.charAt(i))){
                return false;
            } 
               }
               
           }else{
               return false;
           } 
        }
        
    return true;
    }
}