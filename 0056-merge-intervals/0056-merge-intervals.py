class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)

        result = []

        for i, v in enumerate(intervals):
            if result and v[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], v[1])
            else:
                result.append(v)
            
        return result