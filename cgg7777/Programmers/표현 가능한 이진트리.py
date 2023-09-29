def solution(numbers):
    # 무조건 1  3  7  15..자리만 가능
    # 절반 전 까지는 111 101 011  101   1111111 1 1111111
    answer = []
    # 중앙 -> 양옆 한개씩 -> 두개 ->...
    for number in numbers:
        binaryNumber = bin(number)[2:]
        binarylength = len(binaryNumber)
        count = 1
        while (2 ** count < binarylength): count += 1

        gap = 2 ** count - binarylength - 1

        pad = ""
        for i in range(gap):
            pad += "0"

        binaryNumber = pad + binaryNumber
        binaryLength = len(binaryNumber)

        checkFlag = False

        queue = []
        queue.append(binaryLength // 2)

        checkFlag = False

        count -= 1
        beforeZero = False
        while count:
            count -= 1
            length = len(queue)
            while length:
                length -= 1
                current = queue[0]
                queue.pop(0)

                if binaryNumber[current] == "0":
                    if current - 2 ** count >= 0 and binaryNumber[current - 2 ** count] == "1":
                        checkFlag = True
                        break
                    if current + 2 ** count < len(binaryNumber) and binaryNumber[current + 2 ** count] == "1":
                        checkFlag = True
                        break

                queue.append(current - 2 ** count)
                queue.append(current + 2 ** count)

            if checkFlag:
                answer.append(0)
                break

        if not checkFlag:
            answer.append(1)

    return answer