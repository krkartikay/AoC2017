import copy
scanners = {}
length = 0

def main():
	try:
		while True:
			process(raw_input())
	except EOFError:
		analyse_results()

def process(inp):
	l = map(int,inp.split(':'))
	scanners[l[0]] = [0,l[1],1]

def printscanners(j):
	length = max(scanners.keys())+1
	print str(j)+"th picosec"
	for i in range(length):
		if i in scanners:
			#print scanners[i]
			for x in range(scanners[i][1]):
				if i==j and x==0:
					print ("( )" if x!=scanners[i][0] else "(S)"),
				else:
					print ("[ ]" if x!=scanners[i][0] else "[S]"),
		else:
			print "...",
		print ""
	print "="*60

def severity(delay):
	length = max(scanners.keys())+1
	sev = 0
	for i in range(delay):
		for j in range(length):
			if j in scanners:
				if not((scanners[j][0] == scanners[j][1]-1 and scanners[j][2]==1) or (scanners[j][0] == 0 and scanners[j][2]==-1)):
					scanners[j][0] += scanners[j][2]
				else:
					scanners[j][2] *= (-1)
					scanners[j][0] += scanners[j][2]
	#print "After delay %d psec"%delay
	#printscanners(i)
	for i in range(length):
		#printscanners(i)
		if i in scanners:
			if scanners[i][0] == 0:
				return 100
				sev += (i+1)*scanners[i][1]
		for j in range(length):
			if j in scanners:
				if not((scanners[j][0] == scanners[j][1]-1 and scanners[j][2]==1) or (scanners[j][0] == 0 and scanners[j][2]==-1)):
					scanners[j][0] += scanners[j][2]
				else:
					scanners[j][2] *= (-1)
					scanners[j][0] += scanners[j][2]
	return sev

def analyse_results():
	global scanners
	d = 0
	sev = 1
	while sev!=0:
		sev = severity(d)
		d+=2
		reset_scanners()
		if d%1000==0:
			print d
	print d-2

def reset_scanners():
	global scanners
	for key in scanners:
		scanners[key][0] = 0
		scanners[key][2] = 1

main()
