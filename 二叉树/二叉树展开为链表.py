# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []

        def preorder(root):
            if root:
                res.append(root)
                preorder(root.left)
                preorder(root.right)
        
        preorder(root)
        for i in range(1,len(res)):
            l,r = res[i - 1],res[i]
            l.left = None
            l.right = r