class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0],b[0]));
        ArrayList<ArrayList<Integer>> list = new ArrayList<>();
        ArrayList<Integer> subList = new ArrayList<Integer>();
        
        subList.add(intervals[0][0]);
        subList.add(intervals[0][1]);
        list.add(subList);
        
        int i = 1;
        int newI = 0;
        
        while(i<intervals.length){
            subList = new ArrayList<Integer>();
            if(list.get(newI).get(0)==intervals[i][0]||list.get(newI).get(1)>=intervals[i][0]){
                subList.add(list.get(newI).get(0));
                subList.add(Math.max(list.get(newI).get(1),intervals[i][1]));
                list.set(newI,subList);
            }else{
                subList.add(intervals[i][0]);
                subList.add(intervals[i][1]);
                list.add(subList);
                newI++;
            }
            i++;
        }
        int[][] listNew = new int[list.size()][2];
        for(int j=0;j<list.size();j++){
            listNew[j][0] = list.get(j).get(0);
            listNew[j][1] = list.get(j).get(1);
        }
        return listNew;
    }
}