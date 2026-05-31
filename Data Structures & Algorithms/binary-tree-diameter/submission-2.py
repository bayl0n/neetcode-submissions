# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(r):
            nonlocal res 
            if not r:
                return 0

            left_count = dfs(r.left)
            right_count = dfs(r.right)

            res = max(res, left_count + right_count)

            return 1 + max(left_count, right_count)

        dfs(root)

        return res