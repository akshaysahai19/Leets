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
    public ListNode reverseList(ListNode head) {
        if (head != null && head.next != null)
    {
        ListNode pivot = head;
        ListNode frontier = null;
        while (pivot != null && pivot.next != null)
        {
            frontier = pivot.next;
            pivot.next = pivot.next.next;
            frontier.next = head;
            head = frontier;
        }
    }
    
    return head;
    }
}