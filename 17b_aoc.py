class CircularBuffer():
    """Creates a circular buffer with the insert() operation
    as specified in the problem"""
    def __init__(self,stepsize):
        self.stepsize = stepsize
        self.currentPos = 0
        self.maxval = 0
        self.list_ = [0]
    def insert(self):
        self.currentPos += self.stepsize
        self.currentPos %= self.maxval+1
        self.maxval += 1
        self.currentPos += 1
        if self.currentPos == 1:
            self.list_.insert(self.currentPos,self.maxval)
    def __str__(self):
        p = ""
        for i in range(len(self.list_)):
            if i != 0:
                p += " "
            if i != self.currentPos:
                p += str(self.list_[i])
            else:
                p += "("+str(self.list_[i])+")"
        return p

def main():
    c = CircularBuffer(int(raw_input()))
    for x in range(100):
        for y in range(500000):
            c.insert()
        print x
    print c.list_[1]

if __name__ == '__main__':
    main()
