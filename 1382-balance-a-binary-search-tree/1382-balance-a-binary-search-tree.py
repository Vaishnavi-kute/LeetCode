# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = []
         # Step 1 : Inorder traversal to get sorted nodes
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)

        inorder(root)

        #Step 2: Build Balancesd BST from sorted nodes 
        def build(l, r):
            if l  > r:
                return None
            mid = (l + r) // 2
            node = nodes[mid]
            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)
            return node

        return build(0, len(nodes) -1)


        