class Node:
    def __init__(self,name,weight,below=[]):
        self.name = name
        self.weight = weight
        self.below = below
        self.above = None
    def printNode(self,maxlev=-1,level=0):
        if maxlev == -1 or level<maxlev:
            print (" "*4)*level+str(self),"<%d>"%self.totalWeight()
            for nextnode in self.below:
                nextnode.printNode(maxlev,level+1)
    def totalWeight(self):
        if len(self.below)==0:
            return self.weight
        else:
            s = 0
            for nextnode in self.below:
                s += nextnode.totalWeight()
            return s+self.weight
    def __repr__(self):
        if self.above is not None:
            if len(self.below)==0:
                return ("[Leaf Node \"%s\" (%d), below %s]"%(self.name,self.weight,self.above.name))
            return ("[Node \"%s\" (%d), below %s [%d]]"%(self.name,self.weight,self.above.name,len(self.below)))
        else:
            return ("[Root Node \"%s\" (%d),[%d]]"%(self.name,self.weight,len(self.below)))

known_nodes = {}

def process(inp):
    inf = inp.split('->')
    if len(inf)==2:
        left,right = inf
        name = left.split()[0]
        weight = int(left.split('(')[1].split(')')[0])
        right = map(lambda x:x.strip(),right.split(','))
        known_nodes[name] = Node(name,weight,right)
    else:
        left = inf[0]
        name = left.split()[0]
        weight = int(left.split('(')[1].split(')')[0])
        known_nodes[name] = Node(name,weight)

try:
    while True:
        process(raw_input())
except EOFError:
    pass

for name in known_nodes:
    node = known_nodes[name]
    for x in range(len(node.below)):
        node.below[x] = known_nodes[node.below[x]]
        node.below[x].above = node

rootnode = None

for name in known_nodes:
    node = known_nodes[name]
    if node.above is None:
        rootnode = node

def getDifferentNum(givenList):
    avgnum = int(sum(givenList)/len(givenList))
    difflist = map(lambda x:(x-avgnum),givenList)
    m = max(difflist)
    if m != 0:
        x = difflist.index(m)
        return x
    else:
        return None

found = False
while not found:
    weights = map(lambda x: x.totalWeight(),rootnode.below)
    print rootnode
    print weights
    x = getDifferentNum(weights)
    if x is None:
        print rootnode
        found = True
    else:
        rootnode = rootnode.below[x]

rootnode.above.printNode(2)
