class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars_reversed = sorted(zip(position, speed), reverse=True)

        bottleneck = float('-inf')
        fleets = 0

        for distance, speed in cars_reversed:
            remaining_distance = target - distance
            eta = (remaining_distance / speed)

            if eta > bottleneck:
                bottleneck = eta
                fleets += 1

        return fleets