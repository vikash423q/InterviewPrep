from typing import List

#   https://leetcode.com/problems/course-schedule/


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        req = {}
        for preq in prerequisites:
            req.setdefault(preq[0], [])
            req[preq[0]].append(preq[1])

        def dfs(i: int, start: int, visited=None):
            if visited is None:
                visited = set()
            elif i == start:
                return False

            if i in visited:
                return True

            visited.add(i)

            for j in req.get(i, []):
                if not dfs(j, start, visited):
                    return False

            return True

        for i in range(numCourses):
            if not dfs(i, i):
                return False

        return True
