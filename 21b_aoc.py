enhance_rules = {}

def main():
    try:
        while True:
            process(raw_input())
    except EOFError:
        pass
    a = map(list,".#.\n..#\n###".splitlines())
    for i in range(18):
        for x in a:
            for y in x:
                print y,
            print ""
        print "-----------\n"
        if len(a)%2==0:
            newgrid = [["" for x in range((len(a)*3)/2)] for x in range((len(a)*3)/2)]
            for i in range(len(a)/2):
                for j in range(len(a)/2):
                    small_square = [[a[i*2][j*2],a[i*2][j*2+1]],[a[i*2+1][j*2],a[i*2+1][j*2+1]]]
                    new = enhance("/".join("".join(x) for x in small_square))
                    newgrid[i*3+(1-1)][j*3+(1-1)] = new[1-1][1-1]#11
                    newgrid[i*3+(1-1)][j*3+(2-1)] = new[1-1][2-1]#21
                    newgrid[i*3+(1-1)][j*3+(3-1)] = new[1-1][3-1]#31
                    newgrid[i*3+(2-1)][j*3+(1-1)] = new[2-1][1-1]#12
                    newgrid[i*3+(2-1)][j*3+(2-1)] = new[2-1][2-1]#22
                    newgrid[i*3+(2-1)][j*3+(3-1)] = new[2-1][3-1]#32
                    newgrid[i*3+(3-1)][j*3+(1-1)] = new[3-1][1-1]#13
                    newgrid[i*3+(3-1)][j*3+(2-1)] = new[3-1][2-1]#23
                    newgrid[i*3+(3-1)][j*3+(3-1)] = new[3-1][3-1]#33
            a = newgrid
        elif len(a)%3==0:
            newgrid = [["" for x in range((len(a)*4)/3)] for x in range((len(a)*4)/3)]
            for i in range(len(a)/3):
                for j in range(len(a)/3):
                    small_square = [[a[i*3+(1-1)][j*3],a[i*3+(1-1)][j*3+1],a[i*3+(1-1)][j*3+2]],#1
                                    [a[i*3+(2-1)][j*3],a[i*3+(2-1)][j*3+1],a[i*3+(2-1)][j*3+2]],#2
                                    [a[i*3+(3-1)][j*3],a[i*3+(3-1)][j*3+1],a[i*3+(3-1)][j*3+2]]]#3
                    new = enhance("/".join("".join(x) for x in small_square))
                    newgrid[i*4+0][j*4+0] = new[0][0] #00
                    newgrid[i*4+0][j*4+1] = new[0][1] #01
                    newgrid[i*4+0][j*4+2] = new[0][2] #02
                    newgrid[i*4+0][j*4+3] = new[0][3] #03
                    newgrid[i*4+1][j*4+0] = new[1][0] #10
                    newgrid[i*4+1][j*4+1] = new[1][1] #11
                    newgrid[i*4+1][j*4+2] = new[1][2] #12
                    newgrid[i*4+1][j*4+3] = new[1][3] #13
                    newgrid[i*4+2][j*4+0] = new[2][0] #20
                    newgrid[i*4+2][j*4+1] = new[2][1] #21
                    newgrid[i*4+2][j*4+2] = new[2][2] #22
                    newgrid[i*4+2][j*4+3] = new[2][3] #23
                    newgrid[i*4+3][j*4+0] = new[3][0] #30
                    newgrid[i*4+3][j*4+1] = new[3][1] #31
                    newgrid[i*4+3][j*4+2] = new[3][2] #32
                    newgrid[i*4+3][j*4+3] = new[3][3] #33
            a = newgrid
        else:
            print "Error"

        k = 0
        for x in a:
            for y in x:
                if y=='#':
                    k+=1
        print "number of pixels on = %d (%d)"%(k,i)

def process(inp):
    print inp
    s1,s2 = inp.split(' => ')
    for x1 in rots(s1):
        x2 = s2
        print x1,"->",x2
        enhance_rules[x1] = x2

def rev(x):
    if type(x)==list:
        y = list(x[:])
        y.reverse()
        return y
    elif type(x)==str:
        y = list(x[:])
        y.reverse()
        return "".join(y)

def rots(p):
    p = p.split("/")
    z = [range(len(p[0])) for _ in range(len(p[0]))]
    for x in range(len(p[0])):
        for y in range(len(p[0])):
            z[x][y] = p[y][len(p[0])-x-1]
    z = ["".join(x) for x in z]
    return ["/".join(p),
            "/".join(rev(p)),
            "/".join([rev(x) for x in p]),
            "/".join(rev([rev(x) for x in p])),
            "/".join(z),
            "/".join(rev(z)),
            "/".join([rev(x) for x in z]),
            "/".join(rev([rev(x) for x in z])),]

def enhance(inp):
    return map(list,enhance_rules[inp].split('/'))

if __name__ == '__main__':
    main()
