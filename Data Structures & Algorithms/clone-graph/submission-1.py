"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Run bfs, creating a new node for each one visited

        its neighbours list will need to be copied

        when traversing
        -----
        node.val = index + 1
        index = node.val - 1

        perform bfs and for each node 

        O(V^2)

        as we perform bfs and pop off the queue, we copy value and neighbours from current node to new node

        when we return we can just return adj_list[node]

        time complexity: O(V^2)
        space complexity: O(V^2)
        """


        queue = deque()

        queue.append(node)

        if not node:
            return None

        clones = { node: Node(node.val)}

        # perform bfs
        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in clones:
                    new_neighbor = Node(neighbor.val)
                    clones[neighbor] = new_neighbor
                    queue.append(neighbor)

                clones[curr].neighbors.append(clones[neighbor])

        return clones[node]