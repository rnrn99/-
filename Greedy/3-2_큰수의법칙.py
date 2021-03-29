# p.92 큰 수의 법칙
# 첫째 줄에 n, m, k의 자연수가 주어지며 각 자연수는 공백으로 구분한다.
# 둘째 줄에 n개의 자연수가 주어진다.
# 입력으로 주어지는 k는 항상 m보다 작거나 같다.
# 둘째 줄의 배열이 있을 때,  주어진 수들을 M번 더하여 가장 큰 수를 만들어라. 이때 특정 인덱스의 수가 K번을 초과하여 더해질 수 없다.

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = (first * k + second) * int(m / (k+1))

result += first * int(m % (k+1))

print(result)