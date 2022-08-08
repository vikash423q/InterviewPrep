#   https://leetcode.com/problems/min-stack


# using somewhat complicated O(n+1) approach
class MinStack:
    def __init__(self):
        self.arr = []
        self.min_value = None

    def push(self, val: int) -> None:
        if self.min_value and self.min_value > val:
            val, self.min_value = 2 * val - self.min_value, val

        self.arr.append(val)

        if self.min_value is None:
            self.min_value = val

    def pop(self) -> None:
        if not self.arr:
            return
        val = self.arr.pop()
        if val and val < self.min_value:
            self.min_value = 2 * self.min_value - val

    def top(self) -> int:
        if not self.arr:
            return
        val = self.arr[-1]
        if val and val < self.min_value:
            orig_val = self.min_value
            self.min_value = 2 * self.min_value - val
            return orig_val
        return val

    def getMin(self) -> int:
        return self.min_value


#   Using Simpler O(2n) approach
class MinStack2:
    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        if self.arr:
            min_value = min(self.arr[-1][1], val)
        else:
            min_value = val
        self.arr.append((val, min_value))

    def pop(self) -> None:
        if self.arr:
            self.arr.pop()

    def top(self) -> int:
        if self.arr:
            return self.arr[-1][0]

    def getMin(self) -> int:
        if self.arr:
            return self.arr[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
