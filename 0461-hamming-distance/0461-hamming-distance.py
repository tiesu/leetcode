class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = bin(x ^ y)

        count = 0
        for i in result[2:]:
            if i == '1':
                count += 1

        return count