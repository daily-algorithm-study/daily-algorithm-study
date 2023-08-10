import sys

n, T = map(int, sys.stdin.readline().split())

def isPossible(x,y,a,b):
    if abs(a-x) <=2 and abs(y-b) <=2:
        return True
    return False

holes = []
for i in range(n):
    holes.append(list(map(int ,sys.stdin.readline().split())))

holes.sort(key = lambda hole : (hole[1], hole[0]))

q = [[[0,0],0]]
visited = [False for _ in range(len(holes))]
terminateFlag = False
count = -1
while q:
    count += 1
    length = len(q)
    while length:
        currentMetaData = q.pop(0)
        current = currentMetaData[0]
        if current[1] == T:
            terminateFlag = True
            break
        for i in range(currentMetaData[1], -1, -1):
            if not visited[i] and isPossible(current[0], current[1], holes[i][0], holes[i][1]):
                q.append([holes[i], i])
                visited[i] = True
            if abs(current[0] - holes[i][0]) > 2 and abs(current[1] - holes[i][1]) > 2:
                break
        for i in range(currentMetaData[1], len(holes)):
            if not visited[i] and isPossible(current[0], current[1], holes[i][0], holes[i][1]):
                q.append([holes[i], i])
                visited[i] = True
            if abs(current[0] - holes[i][0]) > 2 and abs(current[1] - holes[i][1]) > 2:
                break
        length -= 1
    if terminateFlag:
        break

if terminateFlag:
    print(count)
else:
    print(-1)