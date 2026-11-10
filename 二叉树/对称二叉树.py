# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self,u,v):
        q = deque()
        q.append(u)
        q.append(v)

        while q:
            u = q.popleft()
            v = q.popleft()
            if not u and not v:
                continue
            if (not u or not v) or (u.val != v.val):
                return False

            q.append(u.left)
            q.append(v.right)
            q.append(u.right)
            q.append(v.left)
        return True
    
    def isSymmetric(self, root: TreeNode | None) -> bool:
        return self.func(root,root)    