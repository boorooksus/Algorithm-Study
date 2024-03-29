# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root.left and root.right:
            return root.val if low <= root.val <= high else 0

        res = root.val if low <= root.val <= high else 0

        if root.left:
            res += self.rangeSumBST(root.left, low, high)
        if root.right:
            res += self.rangeSumBST(root.right, low, high)

        return res
