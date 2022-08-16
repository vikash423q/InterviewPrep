from typing import List

#   https://leetcode.com/problems/daily-temperatures/


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        st = []
        res = [0 ] *len(temperatures)
        for i in range(len(temperatures)):
            # top element is less than current pop
            while st and st[-1][0] < temperatures[i]:
                val, idx = st.pop()
                res[idx] += i - idx
            st.append((temperatures[i], i))

        return res
