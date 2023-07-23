# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        past_node = [root]
        count = 0
        while past_node:
            count += 1

            for i in range(len(past_node)):
                cur_node = past_node.pop(0)

                if cur_node.left is not None:
                    past_node.append(cur_node.left)
                
                if cur_node.right is not None:
                    past_node.append(cur_node.right)

        return count
        