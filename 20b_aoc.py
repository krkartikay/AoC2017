import re
pat = re.compile(r'^p=<(.*)>, v=<(.*)>, a=<(.*)>')

l = []
d = []

def main():
    try:
        while True:
            process(raw_input())
    except:
        solve()

def process(arg):
    m = pat.match(arg)
    p,v,a = [tuple(map(int, m.group(x).split(',')))
            for x in range(1,4)]
    l.append((p,v,a))

def dist(pt):
    x,y,z = pt
    x = abs(x)
    y = abs(y)
    z = abs(z)
    return x+y+z

def solve():
    locations = {}
    prevlen = 0
    for tick in range(1000000):
        # check collisions

        for i in range(len(l)):
            p,v,a = l[i]
            v = tuple(v[i] + a[i] for i in range(3))
            p = tuple(p[i] + v[i] for i in range(3))
            l[i] = (p,v,a)
            if p not in locations:
                locations[p] = [i]
            else:
                locations[p] += [i]
            #print "p={},v={},a={}".format(p,v,a)

        for key in locations:
            pts = locations[key]
            if len(pts)>1:
                print "collisions", pts
                for x in pts:
                    l[x] = 0
        try:
            while True:
                l.remove(0)
        except ValueError as e:
            locations = {}

        if len(l) != prevlen:
            prevlen = len(l)
            print "new len,", len(l), "after %d iteration"%tick

main()
