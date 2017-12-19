inp = []

def main():
    global inp
    try:
        while True:
            inp.append(raw_input())
    except EOFError:
        solve(inp)

def up(arg):
    x,y = arg
    return (x,y-1)
def left(arg):
    x,y = arg
    return (x-1,y)
def right(arg):
    x,y = arg
    return (x+1,y)
def down(arg):
    x,y = arg
    return (x,y+1)

def get(sp):
    x,y = sp
    return inp[y][x]

def solve(arg):
    #find starting pt
    sp = (0,0)
    going = down
    symbol = "|"
    letters = ""
    steps = 0
    for x in range(len(inp[0])):
        if inp[0][x] == "|":
            sp = (x,0)
    while symbol != ' ':
        #print sp,get(sp)
        steps += 1
        sp = going(sp)
        symbol = get(sp)
        if symbol == "+":
            # change direction
            if going == up:
                coming_from = down
            if going == down:
                coming_from = up
            if going == left:
                coming_from = right
            if going == right:
                coming_from = left
            dirs = [up,down,left,right]
            for dirc in dirs:
                try:
                    if get(dirc(sp))!=" ":
                        if coming_from != dirc:
                            going = dirc
                except IndexError:
                    pass
        if 'A'<=symbol<='Z':
            letters += symbol
    print steps

main()
