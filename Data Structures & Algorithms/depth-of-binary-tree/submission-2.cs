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
    public int MaxDepth(TreeNode root) {
        var stack = new Stack<(TreeNode, int)>();
        var maxCount = 0;

        stack.Push((root, 1));

        while (stack.Count > 0) {
            (var node, var count) = stack.Pop();

            if (node != null) {
                maxCount = Math.Max(maxCount, count);

                if (node.left != null) stack.Push((node.left, count + 1));
                if (node.right != null) stack.Push((node.right, count + 1));
            }
        }

        return maxCount;

        // if (root == null) return 0;

        // var left = MaxDepth(root.left) + 1;
        // var right = MaxDepth(root.right) + 1;

        // return Math.Max(left, right);
    }
}
