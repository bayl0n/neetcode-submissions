# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count = 0
        self.res = math.inf

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return self.res

        self.kthSmallest(root.left, k)

        self.count += 1

        if self.count >= k:
            self.res = min(root.val, self.res)

        self.kthSmallest(root.right, k)

        return self.res


        