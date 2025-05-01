# [input]
# 첫 번째 줄: N
# N개 줄: 공간의 상태 (0, 1, 2, 3, 4, 5 ,6, 9)

# [output]
# 더 이상 먹을 수 있는 물고기가 없을 때까지 물고기를 잡아먹은 시간

# [조건]
# N은 최대 20

# [풀이]
# graph 2차원 배열 생성
# BFS로 먹을 수 있는 물고기 탐색
# - 없으면 종료
# - 여러 마리이면 가장 위, 그래도 여러 마리면 가장 왼쪽부터 먹는다
# - 아기상어보다 큰 물고기가 있는 칸은 못 지나감

import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 아기 상어 위치 찾기
for x in range(N):
    for y in range(N):
        if space[x][y] == 9:
            shark_pos = (x, y)
            space[x][y] = 0  # 위치를 찾았으면 초기화
            break

# BFS로 먹을 수 있는 물고기 탐색
def bfs(x, y, size):
    visited = [[0] * N for _ in range(N)]
    queue = deque([(x, y)])
    visited[x][y] = 1
    candidates = []

    while queue:
        cx, cy = queue.popleft()

        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                target = space[nx][ny]

                if target <= size:
                    visited[nx][ny] = visited[cx][cy] + 1

                    if 0 < target < size:
                        distance = visited[nx][ny] - 1
                        candidates.append((distance, nx, ny))
                    else:
                        queue.append((nx, ny))

    # 거리, 위쪽, 왼쪽 우선순위로 정렬
    return sorted(candidates, key=lambda x: (x[0], x[1], x[2]))

# 시뮬레이션
def simulate():
    x, y = shark_pos
    size = 2
    eaten = 0
    time_spent = 0

    while True:
        targets = bfs(x, y, size)
        if not targets:
            break

        dist, tx, ty = targets[0]
        time_spent += dist
        eaten += 1
        space[tx][ty] = 0
        x, y = tx, ty

        if eaten == size:
            size += 1
            eaten = 0

    return time_spent

print(simulate())
