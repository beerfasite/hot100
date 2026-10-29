class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for a,b in prerequisites:
            indegree[a] += 1
            adj[b].append(a)
        count = 0
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            selected = q.popleft()
            count += 1
            for nxt in adj[selected]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        return count == numCourses