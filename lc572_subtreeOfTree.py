# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSametree(self, s: TreeNode, t: TreeNode) -> bool:
        if s==None and t==None:
            return True
        elif s==None and t!=None:
            return False
        elif s!=None and t==None:
            return False
        else:
            if s.val == t.val:
                return self.isSametree(s.left, t.left) and self.isSametree(s.right, t.right)
            else:
                return False
            
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if self.isSametree(s, t):
            return 1
        else:
            if s != None:
                return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
            else:
                return False
