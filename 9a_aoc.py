import re

def main():
    inp = raw_input()
    inp = remove_ex_com(inp)
    inp = remove_com(inp)
    score = parse_grps(inp)
    print score

def remove_ex_com(inp):
    return re.sub("!.","",inp)

def remove_com(inp):
    return re.sub("<.*?>","",inp)

# def parse_grps(inp,level=0):
#     print ("  "*level)+"Parsing: ", inp
#
# def get_matching_bracket(inp,index):
#     r = index
#     level = 0
#     while True:
#         if inp[r]=="{":
#             level += 1
#         elif inp[r]==",":
#             pass
#         elif inp[r]=="}":
#             level -= 1
#             if level==0:
#                 return r
#                 break
#         r+=1

# let's do some cheating!! }:-)
def parse_grps(inp):
    inp = inp.replace("{,","{0,")
    inp = inp.replace(",}",",0}")
    l = eval(inp.replace("{","[").replace("}","]"))
    return parse_list(l)

def parse_list(arg,level=1):
    print "  "*(level-1),"Parsing, ", arg
    if arg==0:
        return 0
    s = level
    for x in arg:
        s += parse_list(x,level+1)
    return s

main()
