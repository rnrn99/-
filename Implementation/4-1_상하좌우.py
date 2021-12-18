n = int(input())
data = input().split()

# 상하좌우
s = ["U", "D", "L", "R"]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x = 1
y = 1

for i in data:
    nx = x + dx[s.index(i)]
    ny = y + dy[s.index(i)]

    if(nx <1 or nx >n or ny < 1 or ny > n):
        continue

    x = nx
    y = ny

print(x, y)