""" 
input
    // 조건
        // N×N 크기의 공간
            = 이차원 배열 문제
        // 물고기
            = 총 M마리
            = 크기 1 이상 6 이하
        // 아기 상어 
            = 1마리
            = 초기 크기 2
            = 1초에 상하좌우 한 칸 이동
                = 자신보다 큰 물고기로의 이동 + 섭취 불가
                = 자신보다 작은 물고기로의 이동 + 섭취 가능
                = 자신과 같은 크기의 물고기로의 이동 가능 + 섭취 불가
        // 조건
            // 공간에 먹을 수 있는 물고기가 없다면, 종료
                = 물고기가 없는 경우, 종료
                = 물고기를 모두 섭취한 경우, 종료
                = 물고기가 있지만, 중간 개체 없이 2의 크기 차이를 가지는 경우, 종료
            // 먹을 수 있는 물고기
                = 1마리라면, 그 곳으로 이동
                = 1마리 이상이라면, 거리가 가까운 곳으로 이동
                    = 거리란, 아기상어부터 물고기로의 지나야 하는 칸의 최솟값
                    = 동일한 거리의 물고기 1마리 이상인인 경우, 상단의 물고기를 우선으로 한다
                    = 동일한 거리의 상단의 물고기 1마리 이상인인 경우, 왼쪽의 물고기를 우선으로 한다
        // 이동 = 1초, 섭취 시간 = 0초, 섭취한 경우 빈칸 처리
        // 자신의 크기와 같은 수를 섭취한 경우, 크기 1 증가
        // 몇 초 동안 종료하지 않고, 물고기를 섭취할 수 있는지 출력

    // 첫째 줄: 공간의 크기 N (2 ≤ N ≤ 20)
    // 둘째 줄 ~ n+1 번째 줄: 공간의 상태
        // 공간의 상태값: 0, 1, 2, 3, 4, 5, 6, 9
            // 0: 빈칸
            // 1~6: 물고기의 크기
            // 9: 아기 상어의 위치

output
    // 첫째 줄: 물고기를 섭취할 수 있는 최대 시간

process
    // 시간 제한 2초, 메모리 제한 512MB 고려
    
    // 아기 상어의 초기 위치 저장 변수 선언
        // 탐색의 시작 좌표를 저장
    // 아기 상어의 크기 저장 변수 선언
        = 섭취 시, 크기 증가 및 갱신을 위한 변수
    // 아기 상어 섭취 물고기 수 저장 변수 선언
        = 섭취 시, 갱신 및 크기 증가에 기여하는 변수
            = 크기 증가 시, 0으로 초기화
    // 최대 시간 값 저장 변수 선언
        = 출력 및 갱신을 위한 변수

    // 이차원 배열 생성
        = 공간의 크기 N(2 ≤ N ≤ 20)
    // input 처리에 따른 각 좌표에 물고기, 아기 상어 할당
        = 초기 공간에 1~6의 값이 포함되지 않다면, 조기종료 및 출력 0
        = 초기 공간의 물고기와 아기 상어의 크기가 2이상 차이가 난다면, 조기 종료 및 출력 0
    
    // BFS 함수
        = 탐색 시작 지점 = 아기 상어의 위치

        // 탐색 우선순위 배열
            = 현재 상어의 좌표와 크기를 기준으로 탐색 우선순위 배열 생성

        // 탐색 중 먹을 수 있는 물고기의 좌표 저장
            = 1마리, 해당 좌표 저장
            = 1마리 이상, 가까운 거리부터 저장
                = 상단 우선 -> 좌측 우선 순위 적용

        = 섭취 시, 
            = 섭취 물고기 수 증가
            = 크기와의 값 비교를 통한 크기 증가 판단
                = 크기 증가 시, 섭취 물고기 수 0으로 초기화
                = 크기 증가 시, 탐색 우선순위 배열 갱신을 위한 탐색 
"""

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque
#sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 방향: 상, 하, 좌, 우

shark_x, shark_y = -1, -1
# 아기 상어의 초기 위치 저장 변수
shark_size = 2
# 아기 상어의 크기 변수
eat_count = 0
# 섭취 물고기 수
time = 0
# 최대 시간 값

n = int(input())
# 입력 처리
space = [list(map(int, input().split())) for _ in range(n)]
# input을 처리하여 가로 행 배열을 생성 후, n번 반복하여 이차원 배열 생성

fish = False
# 물고기 존재 여부
eatable_fish = False 
# 4 이상의 물고기만 존재하는지 여부

# 조기 종료 여부 판단
for i in range(n):
    for j in range(n):
        if 1 <= space[i][j] <= 6:
            fish = True
            # 초기 공간에 물고기의 존재 여부 판단
            if 1 <= space[i][j] <= 3:
                eatable_fish = True
                # 4 이상의 물고기만 존재하는지 여부 판단

# 물고기가 아예 없거나, 먹을 수 있는 물고기가 없으면, 조기종료
if not fish or not eatable_fish:
    print(0)
    exit()

# 아기 상어의 초기 위치 파악 및 저장
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            shark_x, shark_y = i, j
            space[i][j] = 0
            # 위치 저장 후, 해당 위치는 이동을 위한 빈칸 처리

def bfs(x, y, size, eat_count, time):
    # 초기 조건 전달

    queue = deque()
    queue.append((x, y, 0))
    # 초기 좌표, 이동거리

    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    # 상어의 초기 위치 방문 처리

    priority = []  
    # 탐색 우선순위 배열

    while queue:
        x, y, dist = queue.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if space[nx][ny] <= size:
                    # 이동 가능한 경우
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
                    # 거리를 더해 탐색 큐에 추가

                    if 1 <= space[nx][ny] <= 6 and space[nx][ny] < size:
                        # 이동 + 섭취 가능한 경우
                        priority.append((dist + 1, nx, ny))
                        # 탐색 우선순위 배열에 추가

    if not priority:
        # 탐색 우선순위 배열이 비어있는 경우
        return x, y, size, eat_count, time, False  
        # 이동 불가


    priority.sort()
    # 거리, 상단, 좌측 순으로 정렬
    dist, nx, ny = priority[0]
    # 우선순위 배열의 첫번째 값 추출

    time += dist
    # 시간 = 이동거리
    eat_count += 1
    # 섭취 물고기 수 증가
    space[nx][ny] = 0  
    # 먹은 자리 빈 칸으로 갱신

    if eat_count == size:
        # 상어 크기 증가 체크 후, 크기 조정 및 섭취 물고기 수 초기화
        size += 1
        eat_count = 0

    return nx, ny, size, eat_count, time, True

# BFS 탐색 실행
while True:
    shark_x, shark_y, shark_size, eat_count, time, can_move = bfs(shark_x, shark_y, shark_size, eat_count, time)

    if not can_move:
        break

print(time) 