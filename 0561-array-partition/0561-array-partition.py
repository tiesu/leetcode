class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        pair_length = int(len(nums)/2)
        nums.sort()
        result = 0
        for i in range(pair_length):
            result += nums[2*i]

        return result