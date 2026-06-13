class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        courses => range(0, numCourses - 1)

        prerequisites[i] = [a, b]
        b -> a
        where b is the prerequisite of a

        goal: if we can take all the courses

        numCourses = 4

        0 -> 1
        |
        v
        2    3

        prerequisites = [[1,0], [2, 0]]

        1 <-> 0

        we can tell if it is impossible if there is a cycle in the graph

        how can we detect if there is a cycle?

        we can perform dfs and if we visit the same node then there is a cycle

        we need to perform dfs on every input
        we can keep track of visited using a hashset

        since we need to return False on a visited node, then
        in reality the time complexity would be O(n) since there is
        no repeated work

        how can we perform dfs using the inputs?
        numCourses = nodes if we take range(numCourses)

        we can try converting the prerequisites to an adjacency list
        """

        adj_list = collections.defaultdict(list)

        for course, prerequisite in prerequisites:
            adj_list[course].append(prerequisite)

        state = [0] * numCourses

        # 0 visited, 1 currently visiting, 2 finished
        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True


            state[course] = 1
            for pre in adj_list[course]:
                if not dfs(pre):
                    return False
            state[course] = 2
            return True


        for c in range(numCourses):
            if not dfs(c):
                return False

        return True