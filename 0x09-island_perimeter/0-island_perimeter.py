#!/usr/bin/python3
'''Task:
0. Island Perimeter
'''


def island_perimeter(grid):
    '''returns the perimeter of the island described'''
    row = len(grid)
    col = len(grid[0])

    island = 0
    shared_edge = 0

    for r in range(row):
        for c in range(col):
            if grid[r][c] == 1:
                island += 1
                if grid[r+1][c] == 1:
                    shared_edge += 1
                if grid[r][c+1] == 1:
                    shared_edge += 1
    return (island * 4) - (shared_edge * 2)
