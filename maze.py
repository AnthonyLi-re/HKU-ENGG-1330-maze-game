# maze.py

def load_maze(file_path):
    with open(file_path, 'r') as file:
        maze = [list(line.strip()) for line in file.readlines()]
    return maze

def display_maze(maze, player_pos):
    for y in range(len(maze)):
        row = ""
        for x in range(len(maze[0])):
            if (y, x) == player_pos:
                row += "P"
            else:
                row += maze[y][x]
        print(row)
