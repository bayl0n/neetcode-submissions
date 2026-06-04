class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        stack = list(sandwiches)
        stack.reverse()
        count = 0

        if not stack or not queue:
            return 0

        while stack and queue:
            if count > len(queue):
                return len(queue)

            currentStudent = queue.popleft()
            currentSandwich = stack.pop()

            if currentStudent != currentSandwich:
                queue.append(currentStudent)
                stack.append(currentSandwich)
                count += 1

            else:
                count = 0

        return len(queue)