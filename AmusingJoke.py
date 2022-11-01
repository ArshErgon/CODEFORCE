
def solve(strOne, strTwo, mainStr):
    alpha_num = [0] * 26
    newString = strOne + strTwo
    for letter in newString:
        idx = ord(letter) - ord('a')
        alpha_num[idx] += 1
    for letter in mainStr:
        idx = ord(letter) - ord('a')
        if alpha_num[idx] == 0:
            return "NO"
        alpha_num[idx] -= 1
    return "YES" if sum(alpha_num) == 0 else "NO"

strOne = input().lower()
strTwo = input().lower()
mainStr = input().lower()

print(solve(strOne, strTwo, mainStr))
    