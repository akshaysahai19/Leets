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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode node = new ListNode();
        node.next = head;
        ListNode fast = head;
        
        int len = 0;
        while(fast!=null){
            len+=1;
            fast=fast.next;
        }
        
        if(len-n==0){
            return node.next.next;
        }
        
        System.out.println(len);
        
        int currentPos = 0;
        while(head!=null){
            if(currentPos+1==(len-n)){
                head.next = head.next.next;
            }
            currentPos+=1;
            head = head.next;
        }
        return node.next;
        
    }
}