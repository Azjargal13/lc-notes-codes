# Maximum Depth of Binary Tree
# or height of tree O(n)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            # call max depth of left subtree
            l_depth = self.maxDepth(root.left)
            # call max depth of right subtree
            r_depth = self.maxDepth(root.right)
            max_depth = max(l_depth, r_depth)
            return max_depth+1


s = Solution()
print(s.maxDepth([3, 9, 20, null, null, 15, 7]))
