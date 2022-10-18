# this file is used for the naming convension of the python files or the problems files name.
name = input().title().replace(' ', '') + ".py"
f = open(name, 'x')
f.write(
    """
def solve(*args, **kwargs):
    return

n = int(input())

print(solve())
    """
)
f.close()