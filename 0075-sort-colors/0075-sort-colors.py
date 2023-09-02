class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # red, white, blue = 0, 1, 2
        index = 0
        now = 0
        length = len(nums)

        while now < length:
            if nums[now] < 1:
                nums[index], nums[now] = nums[now], nums[index]
                index += 1
            if nums[now] > 1:
                length -= 1
                nums[now], nums[length] = nums[length], nums[now]
            else:
                now += 1

