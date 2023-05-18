class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = re.compile("[!?',;.]")
        result = [i for i in re.sub(p, " ", paragraph.lower()).split() if i not in banned]

        return Counter(result).most_common(1)[0][0]

        