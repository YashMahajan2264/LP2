import heapq

class Node:
    def __init__(self, row, col, parent=None):
        self.row = row
        self.col = col
        self.parent = parent
        self.g = 0  # Cost from start node to current node
        self.h = 0  # Heuristic cost from current node to goal node
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f

class AStar:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.start = None
        self.end = None
        self.open_set = []

    def find_path(self, start, end):
        self.start = start
        self.end = end
        self.open_set.append(Node(start[0], start[1]))

        while self.open_set:
            current_node = heapq.heappop(self.open_set)

            if (current_node.row, current_node.col) == end:
                return self.construct_path(current_node)

            neighbors = self.get_neighbors(current_node)

            for neighbor in neighbors:
                tentative_g = current_node.g + 1  # Assuming each step has a cost of 1

                if tentative_g < neighbor.g:
                    neighbor.parent = current_node
                    neighbor.g = tentative_g
                    neighbor.h = self.heuristic(neighbor.row, neighbor.col)
                    neighbor.f = neighbor.g + neighbor.h

                    if neighbor not in self.open_set:
                        heapq.heappush(self.open_set, neighbor)

        return None  # No path found

    def get_neighbors(self, node):
        neighbors = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

        for dr, dc in directions:
            new_row, new_col = node.row + dr, node.col + dc

            if 0 <= new_row < self.rows and 0 <= new_col < self.cols and self.grid[new_row][new_col] != 1:
                neighbors.append(Node(new_row, new_col, node))

        return neighbors

    def heuristic(self, row, col):
        # Using Manhattan distance heuristic
        return abs(row - self.end[0]) + abs(col - self.end[1])

    def construct_path(self, node):
        path = []

        while node:
            path.append((node.row, node.col))
            node = node.parent

        return path[::-1]  # Reverse the path to get it from start to end

# Example usage:
maze_grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

astar = AStar(maze_grid)
start_point = (0, 0)
end_point = (4, 4)
path = astar.find_path(start_point, end_point)
print("Path:", path)
