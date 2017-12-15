import itertools as it

def genA_internal():
    prevval = 65
    factor = 16807
    modulo = 2147483647
    while True:
        newval = (prevval*factor) % modulo
        prevval = newval
        yield newval

def genB_internal():
    prevval = 8921
    factor = 48271
    modulo = 2147483647
    while True:
        newval = (prevval*factor) % modulo
        prevval = newval
        yield newval

def genA():
    ga = genA_internal()
    for value in ga:
        if value%4 == 0:
            yield value

def genB():
    gb = genB_internal()
    for value in gb:
        if value%8 == 0:
            yield value

def main():
    total = 0
    gA,gB = genA(),genB()
    for x in range(5000000):
        a,b = gA.next(), gB.next()
        a,b = bin(a),bin(b)
        a = a[:-17:-1]
        b = b[:-17:-1]
        if a==b:
            total += 1
        if x%10000==0:
            print (x/50000.),"%"
    print total

main()
