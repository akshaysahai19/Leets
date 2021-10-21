class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        int[] newNum = new int[Math.max(nums1.length,nums2.length)];
        HashMap<Integer,Integer> map_nums1 = new HashMap<Integer,Integer>();
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        for(int i=0;i<nums1.length;i++){
            if(map.containsKey(nums1[i])){
                map.put(nums1[i],map.get(nums1[i])+1);
            }else{
                map.put(nums1[i],1);
            }
        }
        int x = 0;
        for(int i=0;i<nums2.length;i++){
            System.out.println("Hello");
            if(map.containsKey(nums2[i])&&map.get(nums2[i])>0){
                map.put(nums2[i],map.get(nums2[i])-1);
                newNum[x]=nums2[i];
                x++;
            }
        }
        return Arrays.copyOf(newNum, x);
    }
}