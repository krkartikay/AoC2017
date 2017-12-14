grid = range(128)
M = 256

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
		print "done, ",s

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
	m = 0
	for l in grid:
		m += l.count("1")
		print l
	print m
	# out = ''
	# for l in grid:
	# 	for x in l:
	# 		if x == '0':
	# 			out += '.'
	# 		elif x == '1':
	# 			out += '#'
	# 	out += '\n'
	# print out

main()
