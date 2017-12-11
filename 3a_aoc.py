num = int(raw_input())

x,y = 0,0
i = 1

def up(x,y):
    return (x,y+1)
def left(x,y):
    return (x-1,y)
def right(x,y):
    return (x+1,y)
def down(x,y):
    return (x,y-1)

directions = [up,left,down,right]
# up = 0, left = 1, down = 2, right = 3
going = 3 # right
steps_to_take = 1
steps_taken = 0

while i<num:
    f = directions[going]
    x,y = f(x,y)
    steps_taken += 1
    if steps_taken==steps_to_take:
        going += 1
        going %= 4
        steps_taken = 0
        if going == 1 or going == 3:
            steps_to_take += 1
    i+=1
print (abs(x)+abs(y))
