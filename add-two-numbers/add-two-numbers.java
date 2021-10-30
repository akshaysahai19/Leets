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
        int carry = 0;
        ListNode sumList = new ListNode();
        ListNode tempList = sumList;
        
        while(l1!=null||l2!=null){
            if(l1!=null&&l2!=null){
                int sum = l1.val+l2.val+carry;
                if(sum>9){
                    carry = (sum/10)%10;
                    sum = sum%10;
                }else{
                    carry=0;
                }
                tempList.next = new ListNode(sum);
                l1 = l1.next;
                l2 = l2.next;
            }else if(l1==null&&l2!=null){
                System.out.println("1");
                int sum = l2.val+carry;
                if(sum>9){
                    carry = (sum/10);
                    sum = sum%10;
                }else{
                    carry=0;
                }
                tempList.next = new ListNode(sum);
                l2 = l2.next;
            }else if(l1!=null&&l2==null){
                int sum = l1.val+carry;
                if(sum>9){
                    carry = (sum/10)%10;
                    sum = sum%10;
                }else{
                    carry=0;
                }
                tempList.next = new ListNode(sum);
                l1 = l1.next;
            }
            tempList = tempList.next;
        }
        if(carry>0){
                tempList.next = new ListNode(carry);
        }
        return sumList.next;
    }
    
}