# A series of equations A / B = k can be seen as a graph in which nodes are the dividend and divisor A and B and weights are the result of the division. So we simply create the graph and traverse it with DFS/BFS to get our result.
#
# Complexity is K * O(N + M) where N and M are the number of nodes and edges, and K is the number of queries. How many nodes can we have? It's 2 * E, where E is the number of equations (2 different nodes per each equation). We can have at most E edges in the graph.
#
# So total complexity is O(K * E), with O(E) additional space for the graph.
# DFS:
class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        def dfs(start, end, path, paths):
            if start == end and start in G:
                paths[0] = path
                return
            if start in vis:
                return
            vis.add(start)
            for node in G[start]:
                dfs(node, end, path * W[start, node], paths)


        G, W = collections.defaultdict(set), collections.defaultdict(float)
        for (A, B), V in zip(equations, values):
            # '|' is set union here. Also equal to G[A].add({B}), G[B].add({A})
            G[A], G[B] = G[A] | {B}, G[B] | {A}
            W[A, B], W[B, A] = V, 1.0 / V

        res = []
        for X, Y in queries:
            paths, vis = [-1.0], set()
            dfs(X, Y, 1.0, paths)
            res += paths[0],
        return res
