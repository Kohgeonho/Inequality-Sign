import sys

def input_single(dtype=int):
    return dtype(sys.stdin.readline().strip())

def input_list(dtype=int):
    return [dtype(i) for i in sys.stdin.readline().strip().split()]

N = input_single()
O = input_list(str)

minS = ''
maxS = ''

minL = maxL = 1
minA, maxB = 0, 9

for o in O:
    if o == ">":
        maxS += "".join(map(str, range(maxB-maxL+1, maxB+1)))
        maxB -= maxL
        maxL = 1

        minL += 1

    elif o == "<":
        minS += "".join(map(str, range(minA+minL-1, minA-1, -1)))
        minA += minL
        minL = 1

        maxL += 1

maxS += "".join(map(str, range(maxB-maxL+1, maxB+1)))
minS += "".join(map(str, range(minA+minL-1, minA-1, -1)))

print(maxS)
print(minS)