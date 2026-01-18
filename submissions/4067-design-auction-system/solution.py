class AuctionSystem:

    def __init__(self):
        self.bids = defaultdict(SortedList)
        self.bids_map = defaultdict(dict)
        

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        self.bids[itemId].add((bidAmount, userId))
        if userId in self.bids_map[itemId]:
            self.bids[itemId].remove((self.bids_map[itemId][userId], userId))
        self.bids_map[itemId][userId] = bidAmount
        

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.addBid(userId, itemId, newAmount)
        

    def removeBid(self, userId: int, itemId: int) -> None:
        self.bids[itemId].remove((self.bids_map[itemId][userId], userId))
        self.bids_map[itemId].pop(userId)

    def getHighestBidder(self, itemId: int) -> int:
        l = self.bids[itemId]
        if l:
            return l[-1][1]
        return -1
        


# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)
