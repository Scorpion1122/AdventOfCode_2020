import fileutility
from grid import Grid


def count_tree_on_path(grid, start_x, step_x, start_y, step_y):
    current_x = start_x + step_x
    current_y = start_y + step_y

    trees_encountered = 0
    while current_y >= 0 and current_y < grid.height:
        grid_item = grid.get_item(current_x, current_y)
        if grid_item == '#':
            trees_encountered += 1

        current_x += step_x
        current_y += step_y

    return trees_encountered


def solve_part_one(grid):
    tree_count = count_tree_on_path(grid, 0, 3, grid.height - 1, -1)
    print(f"Part 1: {tree_count} Trees encountered on path")


def solve_part_two(grid):
    result = count_tree_on_path(grid, 0, 1, grid.height - 1, -1)
    result *= count_tree_on_path(grid, 0, 3, grid.height - 1, -1)
    result *= count_tree_on_path(grid, 0, 5, grid.height - 1, -1)
    result *= count_tree_on_path(grid, 0, 7, grid.height - 1, -1)
    result *= count_tree_on_path(grid, 0, 1, grid.height - 1, -2)
    print(f"Part 2: {result} Multiplied trees encountered on path")


def solve():
    lines = fileutility.read_lines_file("input_day3.txt")
    grid = Grid(lines)

    solve_part_one(grid)
    solve_part_two(grid)



