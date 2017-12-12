import re

total = 0

inp = raw_input()

# garbage_mode = False
# cancel_mode = False
#
# for char in inp:
#     if cancel_mode:
#         cancel_mode = False
#         continue
#     if not garbage_mode:
#         if char == "<":
#             garbage_mode = True
#         else:
#             continue
#     else:
#         if char == "!":
#             cancel_mode = True
#             continue
#         if char != ">":
#             print char,
#             total += 1
#         else:
#             garbage_mode == False

inp = re.sub("!.","",inp)
a = len(inp)
inp = re.sub("<.*?>","<>",inp)
b = len(inp)
print a-b
