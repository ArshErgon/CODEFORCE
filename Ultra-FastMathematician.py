def solve(numOne, numTwo):
    newNum = []
    for idx in range(len(numOne)):
        if numOne[idx] != numTwo[idx]:
            newNum.append("1")
        else:
            newNum.append("0")
    
    return "".join(newNum)

numOne = input()
numTwo = input()
print(solve(numOne, numTwo))