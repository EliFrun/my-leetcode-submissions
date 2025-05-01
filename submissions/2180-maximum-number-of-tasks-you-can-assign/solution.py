class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        left, right = 0, min(len(tasks), len(workers))
        tasks = tasks[:right]
        workers = list(reversed(list(reversed(workers))[:right]))
        right += 1

        def solve(k):
            p = pills
            l = SortedList(workers)
            for task in reversed(tasks[:k]):
                if l[-1] < task:
                    if p == 0:
                        return False
                    i = l.bisect_left(task - strength)
                    try:
                        l.remove(l[i])
                    except:
                        return False
                    p -= 1
                else:
                    l.remove(l[-1])

            return True
                

        ret = -1
        while left <= right:
            mid = (left + right) // 2
            if solve(mid):
                ret = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return min(ret, len(tasks))
