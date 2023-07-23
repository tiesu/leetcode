# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result, past = [], [root]
        
        def maxDepth(root: TreeNode) -> int:
            if root is None:
                return 0
            
            queue = collections.deque([root])
            depth = 0

            while queue:
                depth += 1
                # 큐 연산 추출 노드의 자식 노드 삽입
                for _ in range(len(queue)):
                    cur_root = queue.popleft()
                    if cur_root.left:
                            queue.append(cur_root.left)
                    if cur_root.right:
                            queue.append(cur_root.right)
            # BFS 반복 횟수 == 깊이
            return depth

        while past:
            cur_root = past.pop(0)
            if cur_root:
                past.append(cur_root.left)
                past.append(cur_root.right)
                left_root, right_root = cur_root.left, cur_root.right
                result.append(maxDepth(left_root) + maxDepth(right_root))

        return max(result)