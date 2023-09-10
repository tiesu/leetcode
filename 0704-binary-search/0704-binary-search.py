class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(first, last):
            if first <= last:
                mid_index = (first + last)//2
                middle = nums[mid_index]

                if middle < target:
                    return binary_search(mid_index + 1, last)
                elif middle > target:
                    return binary_search(first, mid_index - 1)
                else:
                    return mid_index
            else:
                return -1

        return binary_search(0, len(nums)-1)