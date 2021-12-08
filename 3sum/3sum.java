class Solution {
    
    HashMap<List<Integer>,Integer> matches = new HashMap<List<Integer>, Integer>();
    
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        for(int i = 0;i<nums.length;i++){
    list = twoSum(Arrays.copyOfRange(nums,i+1,nums.length),nums[i], nums[i], list);
        }
        return list;
    }
    
    public List<List<Integer>> twoSum(int[] nums,int target,int curr,       List<List<Integer>> all_list){
        HashMap<Integer,Integer> map = new HashMap<Integer, Integer>();
        for(int i =0;i<nums.length;i++){
        int complement = -target - nums[i];
            List<Integer> list = new ArrayList<>();
            if(map.containsKey(complement)){
                list.add(curr);
                list.add(complement);
                list.add(nums[i]);
                Collections.sort(list);
                if(!matches.containsKey(list)){
                all_list.add(list);
                    matches.put(list,1);     
                // System.out.println(""+list);               
                }
            }
            map.put(nums[i],i);
        }
        return all_list;
    }
}