class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_user_map = {}
        self.queue = SortedList()
        self.task_priority_map = {}
        for u,t,p in tasks:
            self.add(u,t,p)
        

    def add(self, u: int, t: int, p: int) -> None:
        self.task_user_map[t] = u
        self.queue.add((p,t))
        self.task_priority_map[t] = p
        

    def edit(self, t: int, newPriority: int) -> None:
        p = self.task_priority_map[t]
        self.queue.remove((p, t))
        self.queue.add((newPriority, t))
        self.task_priority_map[t] = newPriority
        

    def rmv(self, taskId: int) -> None:
        p = self.task_priority_map[taskId]
        self.queue.remove((p, taskId))
        

    def execTop(self) -> int:
        if not self.queue:
            return -1
        p, t = self.queue.pop(-1)
        return self.task_user_map[t]


        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
