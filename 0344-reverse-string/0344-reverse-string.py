class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        max_index = len(s) - 1
        for i, v in enumerate(s):
            if i > max_index / 2:
                break
            s[i], s[max_index-i] = s[max_index-i], s[i]