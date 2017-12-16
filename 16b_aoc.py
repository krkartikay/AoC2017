programs = [chr(ord('a')+x) for x in range(16)]

def main():
    try:
        while True:
            i = raw_input()
            # for q in xrange(1000000000):
            #     for x in i.split(','):
            #         process(x)
            #     if (q%10000000==0):
            #         print q/1000000000,'%'
            z = 0
            while z<55: # magic
                for x in i.split(','):
                    process(x)
                print "".join(programs)
                z += 1
    except EOFError:
        analyse_results()

def spin(x):
    global programs
    l = len(programs)
    programs = programs[-x:] + programs
    programs = programs[:l]

def partner(a,b):
    i = programs.index(a)
    j = programs.index(b)
    exchange(i,j)

def exchange(a,b):
    k = programs[a]
    programs[a] = programs[b]
    programs[b] = k

def process(inp):
    if inp[0]=='s':
        spin(int(inp[1:]))
    elif inp[0]=='x':
        a,b = map(int,inp[1:].split('/'))
        exchange(a,b)
    elif inp[0]=='p':
        a,b = inp[1],inp[3]
        partner(a,b)
    #print "".join(programs)

def analyse_results():
    print "".join(programs)

main()
