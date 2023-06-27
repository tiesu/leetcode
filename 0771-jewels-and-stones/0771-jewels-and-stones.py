class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = collections.Counter(stones)

        result = 0
        for i in jewels:
            result += counter[i]
        
        return result