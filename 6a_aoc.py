blocks = tuple(map(int,raw_input().split()))
new_blocks = []
seen_configs = []

def redistribute(blocks):
    ret = list(blocks)
    # perform magic here
    i = ret.index(max(ret))
    j = ret[i]
    k = i
    while j>0:
        i+=1
        i%=len(blocks)
        ret[i]+=1
        ret[k]-=1
        j-=1
    return tuple(ret)

i = 0

while new_blocks not in seen_configs:
    new_blocks = redistribute(blocks)
    seen_configs.append(blocks)
    blocks = new_blocks
    i += 1

print i
