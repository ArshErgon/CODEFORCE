def boy_or_girl(string):
    if len(set(string)) % 2 == 0:
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM!"


string = input()
print(boy_or_girl(string))