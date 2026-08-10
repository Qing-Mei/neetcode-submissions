class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        
        fleets = 0
        slowest_time = 0

        for pos, car_speed in cars:
            arrival_time = (target - pos) / car_speed

            if slowest_time < arrival_time:
                fleets += 1
                slowest_time = arrival_time
        
        return fleets
        