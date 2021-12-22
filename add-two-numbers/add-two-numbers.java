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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int remainder = 0;
        ListNode lsum = new ListNode();
        ListNode lsum_new = lsum;
        while(l1!=null || l2!=null){
            int sum = 0;
            if(l1==null){
                sum=(l2.val+remainder)%10;
                remainder=(l2.val+remainder)/10;
                l2 = l2.next;
            }else if(l2==null){
                sum=(l1.val+remainder)%10;
                remainder=(l1.val+remainder)/10;
                l1 = l1.next;
            }else{
                sum=(l1.val+l2.val+remainder)%10;
                remainder=(l1.val+l2.val+remainder)/10;
                l1 = l1.next;
                l2 = l2.next;
            }
            ListNode temp = new ListNode(sum);
            lsum.next = temp;
            lsum = lsum.next;
        }
        
        if(remainder!=0){
            ListNode temp = new ListNode(remainder);
            lsum.next = temp;
            lsum = lsum.next;
        }
        
        return lsum_new.next;
    }
}