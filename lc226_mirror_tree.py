# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(root: TreeNode):
            if root:
                t=root.left
                root.left=root.right
                root.right=t
            
                if root.left != None:
                    invert(root.left)
                if root.right != None:
                    invert(root.right)
        
        #actual function
        invert(root)
        return root
