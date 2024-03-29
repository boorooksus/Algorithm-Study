from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digs, lets = [], []
        for log in logs:
            if log.split()[1].isnumeric():
                digs.append(log)
            else:
                lets.append(log)

        lets.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return lets + digs
