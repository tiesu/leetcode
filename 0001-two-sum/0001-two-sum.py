import itertools

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        coms = itertools.combinations(nums, 2)
        for com in coms:
            if sum(com) == target:
                index_first = nums.index(com[0])
                return [index_first, nums.index(com[1], index_first+1)]