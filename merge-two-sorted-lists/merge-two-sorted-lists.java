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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode l_1 = new ListNode();
        ListNode l = l_1;
        while(l1!=null&&l2!=null){
            if(l1.val<=l2.val){
                l.next = l1;
                l1 = l1.next;
            }else if(l2.val<l1.val){
                l.next = l2;
                l2 = l2.next;
            }
            l = l.next;
        }
        l.next = l1 == null ? l2 : l1;
        return l_1.next;
    }
}