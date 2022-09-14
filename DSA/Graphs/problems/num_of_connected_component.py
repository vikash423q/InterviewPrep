from typing import List


#   https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        conn = {}
        for edge in edges:
            conn.setdefault(edge[0], [])
            conn.setdefault(edge[1], [])
            conn[edge[0]].append(edge[1])
            conn[edge[1]].append(edge[0])

        def dfs(i: int, visited):
            if i in visited:
                return

            visited.add(i)
            for j in conn.get(i, []):
                dfs(j, visited)

        count = 0
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            dfs(i, visited)
            count += 1

        return count
