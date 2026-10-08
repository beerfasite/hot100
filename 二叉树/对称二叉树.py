# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def func(left,right):
                if left is None and right is None:
                    return True
                if left is None and right is not None:
                    return False
                if left is not None and right is None:
                    return False
                return left.val == right.val and func(left.left,right.right) and func(left.right,right.left)
        return func(root.left,root.right)