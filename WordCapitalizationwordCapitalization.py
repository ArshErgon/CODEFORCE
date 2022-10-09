# Link is here: https://codeforces.com/problemset/problem/281/A

def sol(word):
    if not word[0].isupper():
        word_list = list(word)
        word_list[0] = word_list[0].upper()
        return "".join(word_list)
    return word

word = input()
print(sol(word))
