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
        ListNode resultList = new ListNode();
        ListNode returnList = resultList;
        
        while(l1!=null || l2!=null){
            int result = 0;
            if(l1!=null && l2!=null){
                result = remainder+l1.val+l2.val;
                if(result>9){
                    remainder = result/10;
                    result = result%10; 
                }else{
                    remainder = 0;    
                }
                l1 = l1.next;
                l2 = l2.next;
            }else if(l1!=null){
                result = remainder+l1.val;
                if(result>9){
                    remainder = result/10;
                    result = result%10; 
                }else{
                    remainder = 0;    
                }
                l1 = l1.next;
            }else{
                result = remainder+l2.val;
                if(result>9){
                    remainder = result/10;
                    result = result%10; 
                }else{
                    remainder = 0;    
                }
                l2 = l2.next;
            }
            resultList.next = new ListNode(result);
            resultList = resultList.next;
        }
        if(remainder!=0){
            resultList.next = new ListNode(remainder);    
        }
        
        return returnList.next;
    }
}