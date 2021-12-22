/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public void reorderList(ListNode head) {
        int count = 0;
        ArrayList<Integer> list = new ArrayList<>();
        ListNode l = new ListNode();
        l.next = head;
        l = l.next;
        while(l!=null){
            list.add(l.val);
            l = l.next;
        }
        
        
        int start = 1;
        int end = list.size()-1;
        
        while(start<end){
            head.next = new ListNode(list.get(end));
            head.next.next = new ListNode(list.get(start));
            head = head.next.next;
            end--;
            start++;
        }
        if(list.size()%2==0){
            head.next = new ListNode(list.get(end));
        }
    }
}