class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        waiting_count = 0
        i = 0
        ret = 0
        for bus in buses:
            ret = bus
            while i < len(passengers) and passengers[i] <= bus and waiting_count < capacity:
                waiting_count += 1
                i += 1
            
            if waiting_count == capacity or passengers[i - 1] == ret:
                ret = passengers[i - 1] - 1
                j = i - 1
                while j >= 0 and passengers[j - 1] == ret:
                    j -= 1
                    ret = passengers[j] - 1

            waiting_count = max(0, waiting_count - capacity)

        return ret

            
        
