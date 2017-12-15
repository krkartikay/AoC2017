import itertools as it

def genA():
    prevval = 65
    factor = 16807
    modulo = 2147483647
    while True:
        newval = (prevval*factor) % modulo
        prevval = newval
        yield newval

def genB():
    prevval = 8921
    factor = 48271
    modulo = 2147483647
    while True:
        newval = (prevval*factor) % modulo
        prevval = newval
        yield newval

def main():
    gA,gB = genA(), genB()
    total = 0
    for x in range(40000000):
        a,b = gA.next(), gB.next()
        a,b = bin(a),bin(b)
        a = a[:-17:-1]
        b = b[:-17:-1]
        if a==b:
            total += 1
        if x%10000==0:
            print (x/400000),"%"
    print total

main()
