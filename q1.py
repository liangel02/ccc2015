n = int(input())

inputList = []
result = []

for i in range(0, n, 1):
    input1 = int(input())
    inputList.append(input1)
for i in range(0, len(inputList), 1):
    if inputList[i] == 0:
        del result[-1]
    else:
        result.append(inputList[i])
profit = sum(result)
print(profit)
