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
    for particle in l:
        p,v,a = particle
        # after 1000 ticks
        p = tuple(p[i] + v[i]*1000 + (a[i]*1000**2)/2 for i in range(3))
        d.append(dist(p))
    print d.index(min(d))

main()
