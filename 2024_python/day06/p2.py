import numpy as np


class Grid():
    def __init__(self, lines: list[str]) -> None:
        grid = np.array([], dtype=str)
        for line in lines:
            grid = np.append(grid, list(line))
        grid = np.reshape(grid, (len(lines), len(lines[0])))
        self.grid = grid
        self.direction: int = 0
        self.start = None
        self.routeset = set()

    def change_direction(self) -> None:
        if self.direction == 3:
            self.direction = 0
        else:
            self.direction += 1

    def find_start(self) -> None:
        self.start = np.argwhere(self.grid == '^')[0]
        self.position = (self.start[0], self.start[1])

    def walk(self) -> None:
        y = self.position[0]
        x = self.position[1]
        self.routeset.add((y, x, self.direction))
        blocked_count = 0
        next_pos = -1, -1
        # print(f"Visiting y: {y}, x: {x}")
        while True:
            match self.direction:
                case 0:
                    next_pos = y - 1, x
                case 1:
                    next_pos = y, x + 1
                case 2:
                    next_pos = y + 1, x
                case 3:
                    next_pos = y, x - 1
            # Check bad case
            out_of_bounds = not (0 <= next_pos[0] < self.grid.shape[0]
                                 and 0 <= next_pos[1] < self.grid.shape[1])
            if out_of_bounds or self.grid[next_pos] in ['#', 'O']:
                self.change_direction()
                blocked_count += 1
                if blocked_count == 4:
                    raise RuntimeError("No way out")
            else:
                self.position = next_pos
                y, x = self.position
                blocked_count = 0
                self.routeset.add((y, x, self.direction))
                break

    def find_candidates(self) -> list:
        candidates = []
        for y in range(self.grid.shape[0]):
            for x in range(self.grid.shape[1]):
                if self.grid[y, x] == '.':
                    if self.is_adjacent((y, x)):
                        candidates.append((y, x))
        return candidates

    def is_adjacent(self, position):
        y, x = position
        adjacent_positions = [
            (y - 1, x),
            (y, x + 1),
            (y + 1, x),
            (y, x - 1)
        ]
        for adj_y, adj_x in adjacent_positions:
            if 0 <= adj_y < self.grid.shape[0] and 0 <= adj_x < self.grid.shape[1]:
                if any((adj_y, adj_x, d) in self.routeset for d in range(4)):
                    return True
                if self.grid[adj_y, adj_x] == '^':
                    return True
        return False

    def simulate(self, obstruction):
        y, x = obstruction
        original = self.grid[y, x]

        saved_position = self.position
        saved_direction = self.direction
        saved_routeset = self.routeset.copy()

        self.grid[y, x] = 'O'
        self.find_start()
        self.routeset.clear()
        visited_sim_states = set()

        try:
            while True:
                current_state = (self.position[0], self.position[1], self.direction)
                if current_state in visited_sim_states:
                    break
                visited_sim_states.add(current_state)
                self.walk()
        except (IndexError, RuntimeError):
            pass

        loop_detected = len(self.detect_loop()) > 0
        self.grid[y, x] = original
        self.position = saved_position
        self.direction = saved_direction
        self.routeset = saved_routeset

        return loop_detected

    def detect_loop(self):
        visited = set()
        loops = set()
        for st in self.routeset:
            if st in visited:
                loops.add(st)
            visited.add(st)
        return loops

    def find_loop_obstruction(self):
        candidates = self.find_candidates()
        loop_obstructions = []
        for obstruction in candidates:
            if self.simulate(obstruction):
                loop_obstructions.append(obstruction)
        return loop_obstructions


def main(data):
    score = 0
    lines = data.splitlines()
    grid = Grid(lines)
    grid.find_start()
    visited = set()
    while True:
        try:
            grid.walk()
        except IndexError:
            break
        except RuntimeError:
            break

        new_state = (grid.position[0], grid.position[1], grid.direction)
        if new_state in visited:
            break
        visited.add(new_state)
    print(f"Visited {len(grid.routeset)} cells")
    score = len(grid.find_loop_obstruction())
    print(f"Found {score} loop obstructions")
    return score

