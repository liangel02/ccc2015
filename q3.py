numGates = int(input())
numPlanes = int(input())

gates = []
planes = []
maxNum = 0

for i in range(1, numGates+1):
    gates.append(0)

for i in range(numPlanes):
    n = int(input())
    planes.append(n)

for i in range(len(planes)):
    if gates[planes[i] - 1] == 0:
        gates[planes[i] - 1] = 1
        maxNum = maxNum + 1
    elif gates[planes[i] - 1] == 1:
        for m in range(planes[i] - 1, -1, -1):
            if gates[m] == 0:
                gates[m] = 1
                maxNum = maxNum + 1
                break
            elif m == 0:
                print(maxNum)
                exit()
print(maxNum)
