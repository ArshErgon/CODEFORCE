

def solve(word):
    if len(word) <= 10:
        return word

    word_list = list(word)
    leng_word = len(word) - 2
    return f"{word_list[0]}{leng_word}{word_list[-1]}"


n = int(input())
word_list = []
for i in range(n):
    word_list += [input()]
    

for word in word_list:
    print(solve(word))




