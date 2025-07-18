/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        if(root==null){
            return list;
        }
        return preorderTraversalList(root,list);
    }
    
    public List<Integer> preorderTraversalList(TreeNode root, List<Integer> list) {
        if(root==null){
            return null;
        }
        list.add(root.val);
        preorderTraversalList(root.left,list);
        preorderTraversalList(root.right,list);
        return list;
    }
}