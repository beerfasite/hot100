class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        indegree = [0] * numCourses

        adj = [[] for _ in range(numCourses)]

        #(i,j)j -> i,上了j才能去上i
        for i,j in prerequisites:
            indegree[i] += 1
            adj[j].append(i)


        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        ans = 0
        while q:
            node = q.popleft()
            ans += 1
            for nxt in adj[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        return ans == numCourses
