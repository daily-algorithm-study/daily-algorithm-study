import sys

command = sys.stdin.readline().rstrip()


convertedStr = ""
if "_" in command:
    if command[0] == "_" or command[-1] == "_":
        convertedStr = "Error!"
    else:
        answer = []
        arr = command.split("_")
        count = 0
        for entry in arr:
            if entry == "":
                convertedStr = "Error!"
                break
            for cha in entry:
                if cha.isupper():
                    convertedStr = "Error!"
                    break
            if convertedStr == "Error!":
                break
            if count == 0:
                answer.append(entry[0] + entry[1:])
                count +=1
            else:
                answer.append(entry[0].upper() + entry[1:])
        if convertedStr != "Error!":
            convertedStr = ''.join(answer)

else:
    answer = []
    temp = []
    listedCommand = list(command)
    if listedCommand[0].isupper():
        convertedStr = "Error!"
    else:
        while listedCommand:
            current = listedCommand.pop(0)
            if current == " ":
                convertedStr = "Error!"
                break
            if current.isupper():
                answer.append(''.join(temp))
                temp = []
                temp.append(current.lower())
            else:
                temp.append(current)
        answer.append(''.join(temp))
        if convertedStr != "Error!":
            convertedStr = '_'.join(answer)

print(convertedStr)


