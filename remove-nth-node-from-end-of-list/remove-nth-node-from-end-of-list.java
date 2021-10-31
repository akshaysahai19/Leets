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
        ListNode voidHead = new ListNode(-1);
    voidHead.next = head;
    ListNode p1 = voidHead;
    ListNode p2 = voidHead;
    while (p1.next!=null){
        p1=p1.next;
        if (n--<=0)p2=p2.next;
    }
    if (p2.next!=null) p2.next=p2.next.next;
    return voidHead.next;
    }
}