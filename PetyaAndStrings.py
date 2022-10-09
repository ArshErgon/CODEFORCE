# problem link: https://codeforces.com/problemset/problem/112/A

def sol(str_one, str_two):
    non_duplicate_str_one = set(str_one)
    non_duplicate_str_two = set(str_two)
    str_one_len = sum(ord(x) for x in non_duplicate_str_one)
    str_two_len = sum(ord(x) for x in non_duplicate_str_two)
    print(str_one_len, str_two_len)
    if str_one_len > str_two_len:
        return 1
    elif str_one_len < str_two_len:
        return -1
    else:
        return 0




# str_one = input().lower()
# str_two = input().lower()

str_one = "aslkjlkasdd".lower()
str_two = "asdlkjdajwi".lower()

print(sol(str_one, str_two))
