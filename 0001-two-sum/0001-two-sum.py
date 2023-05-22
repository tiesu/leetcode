class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        combi = itertools.combinations(nums, 2)
        result = ''
        for i in combi:
            if sum(i) == target:
                result = i
                break
        
        result_1 = ''
        result_2 = ''
        
        for i, v in enumerate(nums):
            if v == result[0] and result_1 == '':
                result_1 = i
            if v == result[1] and result_1 != i and result_2 == '':
                result_2 = i
                
        return [result_1, result_2]
                