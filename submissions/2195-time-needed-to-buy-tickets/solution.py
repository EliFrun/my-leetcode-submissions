class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(min(tickets[k], x) for x in tickets) - len([x for x in tickets[k + 1:] if x >= tickets[k]])
        
