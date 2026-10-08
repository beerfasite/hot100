# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        self.res = []
        self.func(root)

        for i in range(1,len(self.res)):
            if self.res[i] <= self.res[i - 1]:
                return False
        return True

    def __init__(self):
        self.res = []
    
    def func(self,root):
        if root is None:
            return
        self.func(root.left)
        self.res.append(root.val)
        self.func(root.right)
    