class SummaryRanges:

    def __init__(self):
        self.l = SortedList()
        

    def addNum(self, value: int) -> None:
        l = self.l
        idx = l.bisect_left([value, value])
        left, right = None, None
        if idx > 0:
            left = l[idx - 1]
        if idx < len(l):
            right = l[idx]
        if not left and not right:
            l.add([value, value])
            return
        
        used = False
        if left:
            if left[0] <= value <= left[1]:
                return
            if value == left[1] + 1:
                used = True
                left[1] = value

        if right:
            if right[0] <= value <= right[1]:
                return
            if value == right[0] - 1:
                used = True
                right[0] = value

        if used and left and right and (left[1] == right[0]):
            l.pop(idx)
            l.pop(idx - 1)
            l.add([left[0], right[1]])     

        if not used:
            l.add([value, value])    

        

    def getIntervals(self) -> List[List[int]]:
        return list(self.l)
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
