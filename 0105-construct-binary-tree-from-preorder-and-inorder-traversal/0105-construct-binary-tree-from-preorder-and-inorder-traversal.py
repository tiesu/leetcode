# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = preorder.pop(0)
        result = TreeNode(val=root)
        inorder_root_index = inorder.index(root)
        
        left_subtree = inorder[:inorder_root_index]
        result.left = self.buildTree(preorder=preorder, inorder=left_subtree)
        right_subtree = inorder[inorder_root_index + 1:]
        result.right = self.buildTree(preorder=preorder, inorder=right_subtree)

        return result