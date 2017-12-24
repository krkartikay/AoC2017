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
    pb = possible_bridges((0,),ports)
    print "Got possible bridges, there are %d of them."%(len(pb))
    maxlen = max(len(b) for b in pb)
    print "The max length is %d."%maxlen
    lb = filter(lambda x:len(x)==maxlen, pb)
    print "The number of bridges with length %d is %d."%(maxlen,len(lb))
    sb = max(strength(b) for b in lb)
    print "The strongest bridge of those has strength %d."%sb

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
