import sys

T = int(sys.stdin.readline())
cases = []
for i in range(T):
    cases.append(int(sys.stdin.readline().rstrip()))

possibles = {3 : 2}
acc = 3
for i in range(3, 45000):
    acc = acc + i
    possibles[acc] = possibles[acc-i] + 1

for entry in cases:
    row = "IMPOSSIBLE"
    for key in possibles:
        if (entry - key) % possibles[key] == 0:
            if key > entry:
                break
            row = str(entry) + " = "
            plus = (entry - key) // possibles[key]
            for i in range(1, possibles[key] + 1):
                if i != possibles[key]:
                    row += str(i+plus) + " + "
                else:
                    row += str(i+plus)
            break
    print(row)
