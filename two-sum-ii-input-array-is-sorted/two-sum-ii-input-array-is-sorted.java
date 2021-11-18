class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] indices = new int[2];
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int i=0;i<numbers.length;i++){
            if(map.containsKey(target-numbers[i])){
                indices[0]=map.get(target-numbers[i])+1;
                indices[1]=i+1;
                return indices;
            }
            map.put(numbers[i],i);
        }
        return indices;
    }
}