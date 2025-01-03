class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([[x[0], x[1], (target - x[0]) / x[1]] for x in zip(position, speed)], key=lambda x: -x[0])

        curr_time_left = 0
        count = 0
        for p, s, time_left in cars:
            if time_left > curr_time_left:
                count += 1
                curr_time_left = time_left
            else:
                continue
        
        return count




        


