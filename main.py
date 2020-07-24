import numpy as np

def readfile(file_name,num_of_grid,num_of_row):
    '''
    :param filename: path/filename of text file
    :param num_of_grid: how many grids(puzzle) in the textfile
    :param num_of_row: how many rows per grid
    :return grids: all grids in a list
    '''
    grids = [] #50x9x9
    file = open(file_name,'r')
    for i in range(num_of_grid):
        grid = []  # 9x9
        title = file.readline() #Grid i
        #print("title",title)
        for j in range(num_of_row): #start from 0
            row = file.readline() #9 no.s
            row_list = [int(item) for item in row if item!='\n']
            #print(row_list)
            grid.append(row_list)
            #print(grid)
            #print("row"+str(j),row)
        # grid_ = np.array(grid)
        # print(grid_.shape)
        grids.append(grid)
    file.close()
    return grids

def print_grid(grid):
    '''
    :param grid: list of rows and columns
    :no return:
    '''
    #grid = np.array(grid)
    #print(grid.shape)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j+1)%3 == 0 and j != 8:
                print(str(grid[i][j])+'|',end="")
            else:
                print(str(grid[i][j])+" ",end="")
        print()
        if (i + 1) % 3 == 0 and i != 8:
            print('-'*(len(grid)*2-1))

def solve(grid):
    pos = find_empty(grid)
    #print("pos",pos)
    if not pos:
        return True # solved
    else:
        row, col = pos
    for num in range(1,10):
        if valid(grid,num,pos):
            grid[row][col] = num #assign number to grid cell
            if solve(grid): #solve again to see if it is solved
                return True
            grid[row][col] = 0
    return False

def find_empty(grid):
    '''
    :param grid: board with rows and cols
    :return (i,j): row and col pos
    '''
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                return (i,j) #row,col
    return None #if fulled

def valid(grid,num,pos):
    '''
    :param grid: board
    :param num: the desired number
    :param pos: (x,y) position
    :return: True/False
    '''
    #check row
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False
    #check col
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    #check 3x3 box
    box_x = pos[0] // 3
    box_y = pos[1] // 3

    for i in range(box_x*3,box_x*3+3):
        for j in range(box_y * 3, box_y * 3 + 3):
            if grid[i][j] == num and pos != (i,j):
                return False
    return True


if __name__ == "__main__":
    num_of_grid = 50
    num_of_col = num_of_row = 9  # rows in 1 full grid
    file_name = "sudoku.txt"
    question_grids = np.array(readfile(file_name, num_of_grid, num_of_row))
    # print(question_grids.shape)
    #print_grid(question_grids[0])
    #print_grid(question_grids[0])
    for i in range(num_of_grid):
        print("solving puzzle",i+1, ":")
        solve(question_grids[i])
        #print("_____________")
        print_grid(question_grids[i])