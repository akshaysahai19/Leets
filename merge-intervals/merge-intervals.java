class Solution {
    
    ArrayList<List<Integer>> list = new ArrayList<>();
    List<Integer> int_list = new ArrayList<>();
    
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (e1, e2) -> Integer.compare(e1[0], e2[0]));
        addIntervals(intervals[0][0],intervals[0][1]);
        int pos=1;
        for(int i=1;i<intervals.length;i++){
            if(intervals[i][0]==list.get(pos-1).get(0)){
                update(Math.max(intervals[i][1], list.get(pos-1).get(1)), 1, pos-1);
            }else{
                if(intervals[i][0]<list.get(pos-1).get(1)||intervals[i][0]==list.get(pos-1).get(1)){
                 update(Math.max(intervals[i][1], list.get(pos-1).get(1)), 1, pos-1);   
                }else{
                    addIntervals(intervals[i][0],intervals[i][1]);
                    pos++;
                }
            }
        }
        
        int[][] new_list = new int[list.size()][2];
        for(int i=0;i<list.size();i++){
            new_list[i][0] = list.get(i).get(0);
            new_list[i][1] = list.get(i).get(1);
        }
        return new_list;
    }   
    
    public void update(int val,int update_index, int main_pos){
        int_list = new ArrayList<>();
        int_list = list.get(main_pos);
        int_list.set(update_index,val);
        list.set(main_pos,int_list);
    }
    
    public void addIntervals(int val1, int val2){
        int_list = new ArrayList<>();
        int_list.add(val1);
        int_list.add(val2);
        list.add(int_list);
    }
}