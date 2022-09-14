from typing import List


#   https://leetcode.com/problems/graph-valid-tree/


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        conn = {}
        for edge in edges:
            conn.setdefault(edge[0], set())
            conn.setdefault(edge[1], set())
            conn[edge[0]].add(edge[1])
            conn[edge[1]].add(edge[0])

        visited = set()

        def bfs(i: int):
            if i in visited:
                return False

            visited.add(i)
            for j in conn.get(i, []):
                conn[j].remove(i)
                if not bfs(j):
                    return False

            return True

        res = bfs(0)
        return res if len(visited) == n else False
