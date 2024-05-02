import heapq

class Node:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = 0

    def __lt__(self, other):
        return self.cost < other.cost

class EightPuzzleSolver:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def solve(self):
        open_set = []
        visited = set()
        heapq.heappush(open_set, Node(self.initial_state))

        while open_set:
            current_node = heapq.heappop(open_set)
            visited.add(tuple(current_node.state))

            if current_node.state == self.goal_state:
                return self.construct_path(current_node)

            for next_state, move in self.get_neighbors(current_node.state):
                if tuple(next_state) not in visited:
                    next_node = Node(next_state, current_node, move, current_node.depth + 1)
                    next_node.cost = next_node.depth + self.heuristic(next_state)
                    heapq.heappush(open_set, next_node)

        return None  # No solution found

    def get_neighbors(self, state):
        neighbors = []
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Left, Right, Up, Down
        empty_row, empty_col = self.find_empty_tile(state)

        for dr, dc in directions:
            new_row, new_col = empty_row + dr, empty_col + dc

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [list(row) for row in state]
                new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
                neighbors.append((new_state, (dr, dc)))

        return neighbors

    def find_empty_tile(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def heuristic(self, state):
        # Manhattan distance heuristic
        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    x, y = divmod(state[i][j] - 1, 3)
                    distance += abs(x - i) + abs(y - j)
        return distance

    def construct_path(self, node):
        path = []
        while node.parent:
            path.append(node.move)
            node = node.parent
        return path[::-1]

# Example usage:
initial_state = [[1, 2, 3],
                 [4, 0, 5],
                 [6, 7, 8]]

goal_state = [[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8]]

solver = EightPuzzleSolver(initial_state, goal_state)
solution = solver.solve()
print("Solution:", solution)
