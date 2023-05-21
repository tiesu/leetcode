class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for val in strs:
            a = "".join(sorted(list(val)))
            if a in result:
                result[a].append(val)
                continue
            result[a] = [val]

        return [v for k, v in result.items()]