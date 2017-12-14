grid = range(128)
M = 256
maxReg = 1

def main():
	try:
		while True:
			process(raw_input())
	except EOFError:
		analyse_results()

def process(inp):
	for i in range(128):
		s = inp+'-'+str(i)
		grid[i] = hash(s)
	print "Done Hashing"

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

def hash(st):
	L = List()
	lengths = map(ord,st)
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
	b = bin(int("".join(["%02x"%i for i in densehash]),16))
	b = b[2:]
	b = "0"*(128-len(b))+b
	return b


def analyse_results():
	global grid
	grid = [list(x) for x in grid]
	grid = [[int(x) for x in l] for l in grid]
	regionate()
	out = ""
	for i in range(len(grid)):
		x = grid[i]
		for j in range(len(grid)):
			q = x[j]
			if q:
				out+= "%03x"%(q)
			else:
				out+= "   "
		out+= "\n"
	print out
	print ""
	print "="*80
	print ""
	print maxReg

def regionate():
	global grid, maxReg
	i = 0
	while i<len(grid):
		j = 0
		while j<len(grid):
			if grid[i][j] == 1:
				maxReg += 1
				fill_region(i,j,maxReg)
			j += 1
		i += 1

def fill_region(i,j,r):
	global grid
	grid[i][j] = r
	adj = [(1,0),(-1,0),(0,1),(0,-1)]
	for (x,y) in adj:
		try:
			z = grid[i+x][j+y]
			if z == 1:
				fill_region(i+x,j+y,r)
			if z != 0 and z != 1 and z != r:
					print "### EMERGENCY, region %03x colliding with %03x" % (z,r)
		except IndexError:
			pass

main()
