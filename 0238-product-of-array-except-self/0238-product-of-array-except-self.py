class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p, r = 1, 1
        out=[1]*len(nums)
        for i, j in zip(range(len(nums)), range(len(nums)-1, -1, -1)):
            out[i] *= p
            p *= nums[i]

            out[j] *= r
            r *= nums[j]

        return out