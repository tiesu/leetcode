class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result = 0
        g.sort()
        s.sort()
        delete_index = None
        for i in range(len(g)):
            for j in range(len(s)):
                if g[i] <= s[j]:
                    result += 1
                    delete_index = j
                    break
            if delete_index is not None:
                s.pop(delete_index)
                delete_index = None

        
        return result