class Game__of__life:
    def __init__(self_modd, grid):
        self_modd.grid = grid

    def count_neighbour_of_cells(self_mod, row, col):
        count = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if (i, j) != (row, col) and 0 <= i < len(self_mod.grid) and 0 <= j < len(self_mod.grid[0]):
                    if self_mod.grid[i][j] == '*':
                        count += 1
        return count

    def rules_of_game_of_life(self_mod):
        new_gridd = [['-' for _ in range(len(self_mod.grid[0]))] for _ in range(len(self_mod.grid))]
        for i in range(len(self_mod.grid)):
            for j in range(len(self_mod.grid[0])):
                count = self_mod.count_neighbour_of_cells(i, j)
                if self_mod.grid[i][j] == '*':
                    if count < 2 or count > 3:
                        new_gridd[i][j] = '-'
                    else:
                        new_gridd[i][j] = '*'
                else:
                    if count == 3:
                        new_gridd[i][j] = '*'
        self_mod.grid = new_gridd

    def display_grid(self_mod):
        for row in self_mod.grid:
            print(' '.join(row))







filename = "input_1.txt"


def read_gridd():
        grid = []
        with open("input_1.txt", 'r') as file:
            for line in file:
                grid.append(list(line.strip()))
        return grid


game = Game__of__life(read_gridd())

print("Test case-1:")
game.display_grid()
print()

num_steps = 1
for step in range(num_steps):
    game.rules_of_game_of_life()
    print(f"After of test case-1:")
    game.display_grid()
    print()

filename = "input_2.txt"


def read_gridd():
        grid = []
        with open("input_2.txt", 'r') as file:
            for line in file:
                grid.append(list(line.strip()))
        return grid


game = Game__of__life(read_gridd())

print("Test case-2:")
game.display_grid()
print()

num_steps = 1
for step in range(num_steps):
    game.rules_of_game_of_life()
    print(f"After of test case-2:")
    game.display_grid()
    print()

filename = "input_3.txt"


def read_gridd():
        grid = []
        with open("input_3.txt", 'r') as file:
            for line in file:
                grid.append(list(line.strip()))
        return grid


game = Game__of__life(read_gridd())

print("Test case-3:")
game.display_grid()
print()

num_steps = 1
for step in range(num_steps):
    game.rules_of_game_of_life()
    print(f"After of test case-3:")
    game.display_grid()
    print()