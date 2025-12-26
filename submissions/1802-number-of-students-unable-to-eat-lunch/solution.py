class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)

        cnt = 0
        l = len(students)
        while cnt <= l:
            s = students.popleft()
            if s == sandwiches[0]:
                cnt = 0
                l = len(students)
                sandwiches.popleft()
            else:
                students.append(s)
            cnt += 1

        return len(students)
        
