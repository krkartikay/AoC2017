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
L = List()
lengths = map(ord,raw_input())
lengths += [17, 31, 73, 47, 23] # HARDCODED
for round in range(64):
    for l in lengths:
        L.reverse(l)
sparsehash = L.l
densehash = range(16)
i = 0
while i<256:
    densehash[i/16] = reduce(lambda x,y:x^y,sparsehash[i:i+16])
    i += 16
print  "".join(["%02x"%i for i in densehash])
