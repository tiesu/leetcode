class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = collections.deque()
        
        for i, v in enumerate(nums):
            while window and window[0] < i - k + 1:
                window.popleft()

            while window and nums[window[-1]] < v:
                window.pop()

            window.append(i)

            if i >= k - 1:
                result.append(nums[window[0]])

        return result



