class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = Counter(nums)
        
        for i, v in result.items():
            if v == 1:
                return i