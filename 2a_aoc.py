spreadsheet = []

try:
    while True:
        spreadsheet.append(map(int,raw_input().split()))
except EOFError:
    pass

minmax = 0

for row in spreadsheet:
    a = max(row)
    b = min(row)
    minmax += (a-b)

print minmax
