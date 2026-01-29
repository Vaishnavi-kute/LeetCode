
class Solution:
    def minimumCost(self, source: str, target: str,
                    original: List[str], changed: List[str],
                    cost: List[int]) -> int:

        INF = 10**18
        # distance matrix for 26 characters
        dist = [[INF] * 26 for _ in range(26)]

        # cost to convert char to itself is 0
        for i in range(26):
            dist[i][i] = 0

        # fill direct conversion costs (take minimum if duplicates exist)
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)

        # Floyd–Warshall to compute all-pairs shortest paths
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # compute total cost
        total_cost = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')
            if dist[u][v] == INF:
                return -1
            total_cost += dist[u][v]

        return total_cost

        