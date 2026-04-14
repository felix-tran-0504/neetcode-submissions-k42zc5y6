# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inOrder(self, root: Optional[TreeNode]) -> list[int]:
        lol = []
        if not root:
            return lol
        if root.left:
            lol = self.inOrder(root.left) + lol
        lol.append(root.val)
        if root.right:
            lol += self.inOrder(root.right)
        return lol

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.inOrder(root)[k-1]