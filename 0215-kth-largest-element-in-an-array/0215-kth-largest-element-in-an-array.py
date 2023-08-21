class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = list(nums)
        heap = []
        for i in h:
            heappush(heap, i)
        
        for i in range(len(h) - k + 1):
            result = heappop(heap)
            
        return result
        