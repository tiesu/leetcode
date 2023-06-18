class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = collections.Counter(s)
        stack = []
        
        for i in s:
            counter[i] -= 1
            
            if i in stack:
                continue
            
            while stack and i < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            
            stack.append(i)
        
        return ''.join(stack)