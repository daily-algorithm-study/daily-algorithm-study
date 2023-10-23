import sys
sys.setrecursionlimit(10000)

def find(a):
    global parent

    if parent[a] == a:
        return a

    return find(parent[a])


def union(a, b):
    global parent
    global rootCount

    a = find(a)
    b = find(b)

    if a == b:
        return rootCount[a]

    if a not in rootCount:
        rootCount[a] = 1

    if b not in rootCount:
        rootCount[b] = 1

    if rootCount[a] >= rootCount[b]:
        rootCount[a] += rootCount[b]
        parent[b] = a
        return rootCount[a]
    else:
        rootCount[b] += rootCount[a]
        parent[a] = b
        return rootCount[b]


T = int(sys.stdin.readline())

for i in range(T):
    parent = {}
    rootCount = {}
    F = int(sys.stdin.readline())
    for j in range(F):
        friends = sys.stdin.readline().split()
        if friends[0] not in parent:
            parent[friends[0]] = friends[0]
        if friends[1] not in parent:
            parent[friends[1]] = friends[1]

        print(union(friends[0], friends[1]))