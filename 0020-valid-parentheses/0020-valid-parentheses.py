class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
    
        brackets = {"}": "{", "]": "[", ")": "("}

        result = []
        for v in s:
            if v in brackets.keys():
                if result and result.pop() == brackets[v]:
                    continue
                else:
                    return False
            elif v in brackets.values():
                result.append(v)

        if result:
            return False
        
        return True
