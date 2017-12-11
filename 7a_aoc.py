class Node:
    def __init__(self,name,weight,below=[]):
        self.name = name
        self.weight = weight
        self.below = below
        self.above = None
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

print rootnode
