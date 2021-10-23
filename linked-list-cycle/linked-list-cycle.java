/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    
    HashMap<ListNode,Boolean> map = new HashMap<ListNode,Boolean>();
    
    public boolean hasCycle(ListNode head) {
        if(head==null||head.next==null){
            return false;
        }
        ListNode nextNode = head.next;
        while(nextNode!=null){
            if(map.containsKey(nextNode)){
                return true;
            }
            map.put(nextNode,true);
            nextNode = nextNode.next;
        }
        return false;
    }

}