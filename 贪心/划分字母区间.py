class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = [0] * 26
        for i,ch in enumerate(s):
            last[ord(ch) - ord('a')] = i
        
        partition = []
        st = ed = 0

        for i,ch in enumerate(s):
            ed = max(ed,last[ord(ch) - ord('a')])

            if i == ed:
                partition.append(ed - st + 1)
                st = ed + 1
        return partition