from itertools import *

num = int(raw_input())

def up(x,y):
    return (x,y+1)
def left(x,y):
    return (x-1,y)
def right(x,y):
    return (x+1,y)
def down(x,y):
    return (x,y-1)

def sum_neighbours(x,y,grid):
    neighbours = list(product([-1,0,1],[-1,0,1]))
    neighbours.remove((0,0))
    s = 0
    for (i,j) in neighbours:
        try:
            s += grid[(x+i,y+j)]
        except KeyError:
            pass
    return s

directions = [up,left,down,right]
# up = 0, left = 1, down = 2, right = 3
going = 3
steps_to_take = 1
steps_taken = 0
x,y = 0,0

j = 1
grid = {(0,0):1}

while j<num:
    f = directions[going]
    x,y = f(x,y)
    j = sum_neighbours(x,y,grid)
    grid[(x,y)] = j
    steps_taken += 1
    if steps_taken==steps_to_take:
        going += 1
        going %= 4
        steps_taken = 0
        if going == 1 or going == 3:
            steps_to_take += 1

print j
