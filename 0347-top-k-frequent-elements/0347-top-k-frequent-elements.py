class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_common = collections.Counter(nums).most_common(k)
        
        return [i[0] for i in most_common]