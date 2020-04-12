# Diameter of Binary Tree
class Solution:
    def height(self, t: TreeNode) -> int:
        if not t:
            return 0
        else:
            return 1+max(self.height(t.left), self.height(t.right))

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        ldia = self.diameterOfBinaryTree(root.left)
        rdia = self.diameterOfBinaryTree(root.right)

        return max(lheight+rheight, max(ldia, rdia))
