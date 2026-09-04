# Read space-separated values of N and M
n, m = map(int, input().split())

# Top half of the door mat
for i in range(1, n, 2):
    print((".|." * i).center(m, '-'))

# Welcome line in the center
print("WELCOME".center(m, '-'))

# Bottom half of the door mat (reverse of the top half)
for i in range(n - 2, 0, -2):
    print((".|." * i).center(m, '-'))
