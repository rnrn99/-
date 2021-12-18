data = input()
row = int(data[1])
col = int(ord(data[0])) - int(ord('a')) + 1

move = [(-2, -1), (-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (-1, 2), (1, 2)]
answer = 0

for m in move:
    nrow = row + m[0]
    ncol = col + m[1]

    if(nrow > 8 or ncol > 8 or nrow < 1 or ncol < 1):
        continue

    answer += 1

print(answer)