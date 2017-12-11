digits = list(raw_input())

l = len(digits)
digits.append(digits[0])
digits = map(int,digits)

repeat_digits = []

for x in range(l-1):
    curt_digit = digits[x]
    next_digit = digits[x+1]
    if curt_digit == next_digit:
        repeat_digits.append(curt_digit)

print sum(repeat_digits)
