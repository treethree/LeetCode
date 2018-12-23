# 1.if node v has not been visited, then mark it as 0.
# 2.if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then their is a ring.
# 3.if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors.

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
