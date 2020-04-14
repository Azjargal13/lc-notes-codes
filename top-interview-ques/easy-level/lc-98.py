# Validate Binary Search Tree


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isBST(root, l=None, r=None):
            if root == None:
                return True
            if l != None and root.val <= l.val:
                return False
            if r != None and r.val <= root.val:
                return False

            return isBST(root.left, l, root) and isBST(root.right, root, r)
        return isBST(root)
