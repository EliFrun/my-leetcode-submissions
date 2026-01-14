class SegTree:
    def __init__(self, left, right, count, lis):
        self.left = left
        self.right = right
        self.left_n = None
        self.right_n = None
        self.area = 0
        self.active_area = 0
        if right - left > 0:
            self.left_n = SegTree(left, left + (right - left)//2, count, lis)
            self.right_n = SegTree(left + (right - left)//2 + 1, right, count, lis)
            self.area = self.left_n.area + self.right_n.area
        else:
            self.area = lis[left]
        self.count = 0


    def insert(self, left, right):
        if self.left > right:
            return
        if self.right < left:
            return

        if left <= self.left and self.right <= right:
            self.count += 1
            self.active_area = self.area
            return

        self.left_n.insert(left, right)
        self.right_n.insert(left, right)
        if self.count == 0:
            self.active_area = self.left_n.active_area + self.right_n.active_area


    def remove(self, left, right):
        if self.left > right:
            return
        if self.right < left:
            return

        if left <= self.left and self.right <= right:
            self.count -= 1
            if self.count == 0:
                if self.right - self.left > 0:
                    self.active_area = self.left_n.active_area + self.right_n.active_area
                else:
                    self.active_area = 0
            return

        self.left_n.remove(left, right)
        self.right_n.remove(left, right)
        if self.count == 0:
            self.active_area = self.left_n.active_area + self.right_n.active_area

    def __str__(self):
        return f'{self.left}->{self.right}: {self.active_area}/{self.area} ' + (str(self.left_n) if self.left_n else '') + (str(self.right_n) if self.right_n else '')
        

    




class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        distinct_x = set()
        for x,y,l in squares:
            distinct_x.update([x, x + l])

        distinct_x = SortedList(list(distinct_x))
        diff = [distinct_x[i + 1] - distinct_x[i] for i in range(len(distinct_x) - 1)]

        s = SegTree(0, len(diff) - 1, 0, diff)


        y_events = defaultdict(list)
        for x,y,l in squares:
            l_idx = distinct_x.index(x)
            r_idx = distinct_x.index(x + l) - 1
            y_events[y].append((1, l_idx, r_idx))
            y_events[y + l].append((-1, l_idx, r_idx))


        total_area = 0
        prev = 0
        for y in sorted(y_events.keys()):
            total_area += (y - prev) * s.active_area
            for t, left, right in y_events[y]:
                if t == 1:
                    s.insert(left, right)
                if t == -1:
                    s.remove(left, right)
            prev = y

        target_area = total_area / 2


        curr = 0
        prev = 0
        for y in sorted(y_events.keys()):
            diff = (y - prev) * s.active_area
            if curr + diff > target_area:
                return (target_area - curr)/s.active_area + prev
            curr += diff
            if curr == target_area:
                return y
            for t, left, right in y_events[y]:
                if t == 1:
                    s.insert(left, right)
                if t == -1:
                    s.remove(left, right)
            prev = y
            
        return -1
        
            
        
