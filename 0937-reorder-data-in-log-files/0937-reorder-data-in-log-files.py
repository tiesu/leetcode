class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig, let = [], []
        for log in logs:
            a = "".join(log.split()[1:])
            if a.isdigit():
                dig.append(log)
            else:
                let.append(log)

        let1 = [v.split() for v in let]
        let1.sort(key=lambda x: (x[1:], x[0]))
        let = [" ".join(v) for v in let1]

        return let + dig