from typing import List


#   https://leetcode.com/problems/car-fleet/


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [(pos, sp) for pos, sp in zip(position, speed)]
        pos_speed.sort(key=lambda ps: -ps[0])

        fleet = 0
        m = 0
        for p, s in pos_speed:
            if (target - p) / s > m:
                m = (target - p) / s
                fleet += 1

        return fleet
