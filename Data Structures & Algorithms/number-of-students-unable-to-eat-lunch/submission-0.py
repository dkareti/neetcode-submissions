from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """Find the number of students who are unable to eat."""
        #stack of sandwiches never changes, but the queue of students can shift
        #   first student goes to end of queue: new = students[1:] + students[:1]
        students = deque(students)
        sandwiches = deque(sandwiches)
        while sandwiches and sandwiches[0] in students:
            #there is a student who perfers the sandwich
            if students[0] != sandwiches[0]:
                students.append(students.popleft())
            else:
                students.popleft()
                sandwiches.popleft()

        return len(students)