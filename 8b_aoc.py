registers = {}
max_reg = 0

def main():
    try:
        while True:
            process(raw_input())
            analyze_results()
    except EOFError:
        print max_reg

def process(st):
    sp = st.split()
    if sp[0] not in registers:
        registers[sp[0]] = 0
    if sp[4] not in registers:
        registers[sp[4]] = 0
    if eval(str(registers[sp[4]])+sp[5]+sp[6]):
        registers[sp[0]] += (int(sp[2]) if sp[1]=="inc" else -int(sp[2]))

def analyze_results():
    global max_reg
    v = registers.values()
    v.append(max_reg)
    max_reg = max(v)

main()
