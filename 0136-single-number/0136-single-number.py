class Solution:
    def singleNumber(self, nums: List[int]) -> int:
#         result = Counter(nums)
        
#         for i, v in result.items():
#             if v == 1:
#                 return i

        result = 0
        for i in nums:
            result ^= i
            
        return result