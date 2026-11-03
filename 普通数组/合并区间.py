class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        intervals.sort()
        ans = []
        st = intervals[0][0]
        ed = intervals[0][1]
        
        for i in range(1,len(intervals)):
            nxt_st = intervals[i][0]
            nxt_ed = intervals[i][1]

            if nxt_st <= ed:
                #有重叠
                ed = max(ed,nxt_ed)
            else:
                #没有重叠
                ans.append([st,ed])
                st = nxt_st
                ed = nxt_ed

        ans.append([st,ed])

        return ans
