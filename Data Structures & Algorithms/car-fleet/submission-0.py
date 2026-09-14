class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        prev_time = 0
        fleet_len = 0
        cars = list(zip(position,speed))
        cars.sort(reverse=True)
        for pos, spd in cars:
            curr_time = (target - pos) / spd

            if curr_time > prev_time:
                fleet_len += 1
                prev_time = curr_time
        return fleet_len


        
        