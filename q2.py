n = int(input())
p = int(input())

jerseys = []
athleteRequests = []
maxRequests = 0

for i in range(n):
    inputJ = input()
    inputJ = inputJ.upper()
    jerseys.append(inputJ)

for i in range(p):
    athlete = input()
    a = athlete.split(" ")
    athleteRequests.append(a[0])
    athleteRequests.append(a[1])

for i in range(0, len(athleteRequests), 2):
    a = int(athleteRequests[i+1]) - 1
    if athleteRequests[i] == "S":
        if jerseys[a] == "S" or jerseys[a] == "M" or jerseys[a] == "L":
            jerseys[a] = "T"
            maxRequests = maxRequests + 1
    elif athleteRequests[i] == "M":
        if jerseys[a] == "M" or jerseys[a] == "L":
            jerseys[a] = "T"
            maxRequests = maxRequests + 1
    elif athleteRequests[i] == "L":
        if jerseys[a] == "L":
            jerseys[a] = "T"
            maxRequests = maxRequests + 1

print(maxRequests)
