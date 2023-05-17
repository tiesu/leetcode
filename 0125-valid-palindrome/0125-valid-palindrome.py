class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        p = re.compile("[a-zA-Z0-9]")
        s = p.findall(s)

        return True if s[::-1] == s else False
        