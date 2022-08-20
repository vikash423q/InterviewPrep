from typing import List


#   https://leetcode.com/problems/detect-squares/


class DetectSquares:

    def __init__(self):
        self.coord = {}
        self.x_point = {}

    def add(self, point: List[int]) -> None:
        self.coord[tuple(point)] = 1 + self.coord.get(tuple(point), 0)
        self.x_point.setdefault(point[0], set())
        self.x_point[point[0]].add(point[1])

    def count(self, point: List[int]) -> int:
        x, y = point
        c = 0
        for yp in self.x_point.get(x, []):
            if yp == y:
                continue

            cyp = self.coord[(x, yp)]
            # side of square
            a = abs(yp - y)
            c += self.coord.get((x + a, y), 0) * self.coord.get((x + a, yp), 0) * cyp
            c += self.coord.get((x - a, y), 0) * self.coord.get((x - a, yp), 0) * cyp

        return c

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
