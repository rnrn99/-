n, m = map(int, input().split()) # n * m의 맵이 입력으로 들어옴
x, y, direction = map(int, input().split()) # 현재 캐릭터가 있는 x, y 좌표와 보는 방향(0북 1동 2남 3서)
arr_map = [] # 맵 정보
for i in range(n):
    arr_map.append(list(map(int, input().split())))

visit = [[0] * m for _ in range(n)] # 방문할 곳을 저장하기 위한 n * m의 맵 생성. 모든 값은 0으로 초기화
visit[x][y] = 1 # 현재 위치 방문 처리

dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]

def turnLeft():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1 # 움직인 횟수
turnTime = 0 # 회전한 횟수

while True:
    turnLeft() # 1단계 왼쪽 회전
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전 이후 방문한 곳이 아니고 바다가 아닐 경우 방문
    if visit[nx][ny] == 0 and arr_map[nx][ny] == 0:
        visit[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turnTime = 0
        continue
    # 회전 이후 방문할 곳이 없을 경우
    else:
        turnTime += 1

    # 현재 위치에서 동서남북 아무데도 방문할 곳이 없을 경우
    if turnTime == 4:
        nx = x - dx[direction] # 3단계에 따라 바라보는 방향을 유지한 채 한칸 뒤를 확인
        ny = y - dy[direction]

        # 확인할 곳이 바다가 아닐 경우 이동
        if arr_map[nx][ny] == 0: 
            x, y = nx, ny
        # 바다가 아닌 경우 움직일 곳이 더이상 없으므로 움직임 종료
        else:
            break

        turnTime = 0
print(count)