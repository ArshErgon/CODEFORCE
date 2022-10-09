# problem link: https://codeforces.com/problemset/problem/282/A


def sol(bit_string):
    count = 0
    cal = {
        '+': + 1,
        '-': - 1
    }
    for bit in bit_string:
        count += cal[bit[1]]

    return count

n = int(input())

bit_string = []
for i in range(n):
    bit_string.append(input())

print(sol(bit_string))