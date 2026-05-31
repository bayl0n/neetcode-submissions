/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
    public TreeNode InvertTree(TreeNode root) {
        if (root == null)
            return null;
            
        var stack = new Stack<TreeNode>();

        stack.Push(root);

        while (stack.Count > 0) {
            var currentNode = stack.Pop();

            (currentNode.left, currentNode.right) = (currentNode.right, currentNode.left);

            if (currentNode.left != null) {
                stack.Push(currentNode.left);
            }

            if (currentNode.right != null) {
                stack.Push(currentNode.right);
            }
        }

        return root;
    }
}
