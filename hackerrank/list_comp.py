
#algorithm link: https://www.hackerrank.com/challenges/list-comprehensions/problem

#solution
x = int(input())
y = int(input())
z = int(input())
n = int(input())

koordinatlar = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(koordinatlar)
