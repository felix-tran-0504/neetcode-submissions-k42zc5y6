# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def max_val(root):
            if not root:
                return float("-inf")
            while root.right:
                root = root.right
            return root.val
        def min_val(root):
            if not root:
                return float("inf")
            while root.left:
                root = root.left
            return root.val

        if not root:
            return True
        if self.isValidBST(root.left) and self.isValidBST(root.right):
            return (max_val(root.left) < root.val and min_val(root.right) > root.val)
        return False

         