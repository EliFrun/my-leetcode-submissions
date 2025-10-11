class ExamTracker:

    def __init__(self):
        self.l = SortedList([(0,0)])
        

    def record(self, time: int, score: int) -> None:
        t, s = self.l[-1]
        self.l.add((time, s + score))
        

    def totalScore(self, startTime: int, endTime: int) -> int:
        l = self.l
        left_idx = l.bisect_left((startTime, -1))
        if l[left_idx][0] == startTime and left_idx > 0:
            left_idx -= 1

        if left_idx > 0 and l[left_idx][0] > startTime and l[left_idx - 1][0] < startTime:
            left_idx -= 1
        
        right_idx = l.bisect_right((endTime, float('inf')))
        if right_idx >= len(l):
            right_idx -= 1
        elif right_idx < len(l) and l[right_idx][0] > endTime:
            right_idx -= 1
        return l[right_idx][1] - l[left_idx][1]
        


# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)
