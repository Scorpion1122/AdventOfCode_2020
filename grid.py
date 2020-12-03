from array import *


# 0,0 is the top left
class Grid:

    def __init__(self, lines):
        self.width = len(lines[0])
        self.height = len(lines)
        self.grid_data = []

        for line in lines:
            row = []
            for character in line:
                row.append(character)
            self.grid_data.insert(0, row)

    def get_item(self, x, y):
        x = x % self.width
        return self.grid_data[y][x]

    def print_row(self, x, y):
        clamped_x = x % self.width

        line = ""
        for x_i in range(self.width):
            item = self.grid_data[y][x_i]
            if clamped_x == x_i and item == '#':
                line += 'X'
            elif clamped_x == x_i:
                line += 'O'
            else:
                line += item

        print(f"{line}  ({clamped_x}:{x},{y})")
