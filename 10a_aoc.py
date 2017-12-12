M = 256

class List():
    def __init__(self):
        self.l = range(M)
        self.currentPos = 0
        self.skipSize = 0
    def reverse(self, length):
        elms = [self.l[(self.currentPos+x)%M] for x in range(length)]
        elms.reverse()
        for x in range(length):
            self.l[(self.currentPos+x)%M] = elms[x]
        self.currentPos += (self.skipSize + length)
        self.currentPos %= M
        self.skipSize += 1
    def __repr__(self):
        s = "["
        for x in range(M):
            if x == self.currentPos:
                s+=" ("+str(self.l[x])+") "
            else:
                s+=" "+str(self.l[x])+" "
        s += "] (%d)"%self.skipSize
        return s

lengths = map(int, raw_input().split(','))

L = List()
for l in lengths:
    L.reverse(l)
    print L
