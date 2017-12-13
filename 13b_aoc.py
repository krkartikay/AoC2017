import copy

scanners = {}

def main():
	try:
		while True:
			process(raw_input())
	except EOFError:
		analyse_results()

def process(inp):
	l = map(int,inp.split(':'))
	scanners[l[0]] = l[1]

def analyse_results():
	m = range(10000000)
	def f(x):
		for s in scanners:
			if ((x+s)%(2*(scanners[s]-1)))==0:
				return False
		return True
	m = filter(f,m)
	print m


main()
