spreadsheet = []

try:
    while True:
        spreadsheet.append(map(int,raw_input().split()))
except EOFError:
    pass

answer = 0

for row in spreadsheet:
    l = len(row)
    for a in row:
        for b in row:
            if b%a==0 and b!=a:
                answer+=(b/a)
print answer
