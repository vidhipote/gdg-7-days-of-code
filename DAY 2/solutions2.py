n = int(input(" "))
for i in range(1, n + 1):
    star = 2 * i - 1
    space = n - i
    print(' ' * space + '*' * star)
