# p.96 숫자 카드 게임

n, m = map(int, input().split())

result = 0
num = 0

for i in range(n):
    data = list(map(int, input().split()))
    num = min(data)
    result = max(result, num)

print(result)