class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            current_gas = gas[i] - cost[i]
            j = (i + 1) % len(gas)
            while j != i and current_gas >= 0:
                current_gas += gas[j] - cost[j]
                j = (j + 1) % len(gas)
                
            if current_gas >= 0:
                return i
            
            
        return -1
                
