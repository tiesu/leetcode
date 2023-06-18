class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        for index, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                last = stack.pop()
                result[last] = index - last

            stack.append(index)

        return result