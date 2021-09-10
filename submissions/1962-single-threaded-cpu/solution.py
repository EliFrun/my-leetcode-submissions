class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
            tasks = [(x[0], x[1], i) for i, x in enumerate(tasks)]
            tasks.sort()
            curr_time = 0
            ret = []
            h = []
            heapify(h)
            i = 0
            while i < len(tasks):
                while i < len(tasks) and tasks[i][0] <= curr_time:
                    heappush(h, (tasks[i][1], tasks[i][2]))
                    i += 1
                    
                if h:
                    foo = heappop(h)
                    ret.append(foo[1])
                    curr_time += foo[0]
                else:
                    curr_time = tasks[i][0]
                    
            while h:
                foo = heappop(h)
                ret.append(foo[1])
                curr_time += foo[0]
                
            return ret
