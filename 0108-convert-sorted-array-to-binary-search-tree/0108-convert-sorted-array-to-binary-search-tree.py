# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def get_middle_node(nums: List[int]) -> Optional[TreeNode]:
            if not nums:
                return None

            middle_index = int(len(nums)/2)
            result = TreeNode(
                val=nums[middle_index], 
                left=get_middle_node(nums[:middle_index]) if middle_index else None, 
                right=get_middle_node(nums[middle_index+1:])
            )
            
            return result
        
        return get_middle_node(nums)