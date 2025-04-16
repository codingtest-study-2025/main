# [input]
# 첫번째 줄 - N, M, R, C (N, M은 지도의 크기, R은 방 개수, C는 편의점 개수)
# 두번째 줄 ~ R개의 줄 - a, b, p (x, y, 월세)
# R+2번째 줄 ~ C개 줄 - c, d (편의점 위치)

# [output]
# 가장 낮은 점수 출력

# [참고]
# 방과 편의점은 각각 1개 이상 존재한다.
# 모든 방과 편의점 위치는 서로 다르다 (겹칠 일 없다)
# 편세권 점수 = (방에서 가장 가까운 편의점까지의 거리 x 월세)
# 거리는 |a-c| + |b-d|로 계산

# [제한]
# 2 <= N, M <= 1,000
# 1 <= p <= 100

# [풀이방법]
# 모든 방에 대한 편의점 위치 점수를 다 계산하면 시간초과
# 편의점마다 bfs를 수행해서 N x M 맵에 방마다 최소 거리 기록
# 방의 위치마다 점수 계산 후 최소 점수 출력

import sys
from collections import deque

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M, R, C = list(map(int, input().split(' ')))
rooms = []
INF = 10000000000

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque()

dist = [[INF] * (M + 1) for _ in range(N + 1)]

for _ in range(R):
    a, b, p = list(map(int, input().split(' ')))
    rooms.append((a, b, p))

for _ in range(C):
    c, d = list(map(int, input().split(' ')))
    dist[c][d] = 0  # 거리 초기화
    queue.append((c, d))  # 큐에 편의점 위치 넣기


while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 지도 범위 내에 있는지 확인 (1 ≤ nx ≤ N, 1 ≤ ny ≤ M)
        if 1 <= nx <= N and 1 <= ny <= M:
            if dist[nx][ny] > dist[x][y] + 1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))


# 모든 방에 대해 (방에서 가장 가까운 편의점까지의 거리) × (월세)의 값을 계산하고, 최소 점수를 찾음.
min_score = INF
for idx, (a, b, c) in enumerate(rooms):
    score = dist[a][b] * c
    if score < min_score:
        min_score = score

print(min_score)
