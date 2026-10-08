class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        self.dfs(s,[],res,0)
        return res


    def huiwen(self,s,st,ed):
        i = st
        j = ed
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True



    def dfs(self,s,path,res,stindex):
        if stindex == len(s):
            res.append(path[:])
            return

        for i in range(stindex,len(s)):
            if self.huiwen(s,stindex,i):
                path.append(s[stindex:
                i + 1])
                self.dfs(s,path,res,i+1)
                path.pop()
        