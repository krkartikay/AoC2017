ports = []

def main():
    try:
        while True:
            process(raw_input())
    except EOFError:
        solve()

def process(arg):
    ports.append(tuple(int(x) for x in arg.split("/")))

def solve():
    print max(strength(bridge) for bridge in possible_bridges((0,),ports))

def strength(bridge):
    return 2*sum(bridge)-bridge[0]-bridge[-1]

def possible_bridges(beginning,pieces):
    bridges = [beginning]
    #print beginning, pieces
    if len(pieces)==0:
        return bridges
    for (x,y) in pieces:
        if beginning[-1] == x:
            new = beginning + (y,)
            z = pieces[:]
            z.remove((x,y))
            bridges += possible_bridges(new, z)
        elif beginning[-1] == y:
            new = beginning + (x,)
            z = pieces[:]
            z.remove((x,y))
            bridges += possible_bridges(new, z)
        else:
            pass
    return bridges

main()
