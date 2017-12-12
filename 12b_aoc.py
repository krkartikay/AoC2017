programs = {}

def main():
    try:
        while True:
            process(raw_input())
    except EOFError:
        collect_sets()
        analyse_results()

def process(inp):
    inp = inp.replace(","," ").split()
    inp += [""] # evil hack; but why do we need it?
    programs[inp[0]] = set(inp[2:-1])

def collect_sets():
    for key in programs:
        value = programs[key]
        for prog in value:
            set_a = programs[key]
            set_b = programs[prog]
            set_u = set_a.union(set_b)
            programs[key] = set_u
            programs[prog] = set_u

def analyse_results():
    import time
    numgrps = 0
    #while True:
    keys = programs.keys()
    for key in keys:
        try:
            s = programs[key]
            for p in s:
                if p!=key:
                    programs.pop(p)
        except KeyError:
            pass
    print len(programs)

main()
