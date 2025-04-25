""" 
input
    // 조건
        // n x n 크기의 대나무 숲
            = 이차원 배열 문제
        // 판다는 어떤 지역에서 대나무를 먹기 시작한다.
            = 특정 위치로부터 탐색 시작
        // 다 먹어 치우면 상하좌우 중 한 곳으로 이동
            = 탐색이 완료된 경우, 주변으로의 탐색 시작
        // 조건
            // 다음 지역의 대나무는 이전 지역의 대나무보다 많아야 한다
        // 어떤 지점에 처음에 풀어 놓아야 하고,
            = 탐색 시작 지점이 정해져 있지 않음
        // 어떤 곳으로 이동을 시켜야 최대한 많은 칸을 방문할 수 있는지
            = 탐색의 최대 depth 
        //  n × n 크기의 대나무 숲이 주어져 있을 때, 이 판다가 최대한 많은 칸을 이동하려면 어떤 경로를 통하여 움직여야 하는지 구하여라.
            = 이차원 배열에서 탐색 지점, 가능한 최대 탐색 depth, 탐색 루트

    // 첫째 줄: 대나무 숲의 크기 n(1 ≤ n ≤ 500)
    // 둘째 줄 ~ n+1 번째 줄: 대나무 숲의 정보
        // 공백을 기준으로 대나무(n =< 1,000,000)의 양을 정수로 제공

output
    // 첫째 줄: 이동 가능한 칸의 최댓값 출력

process
    // 시간 제한 2초 고려
    
    // 이차원 배열 생성
        // 대나무 숲의 크기 n(1 ≤ n ≤ 500)
    // 최대 탐색 값 저장 변수
        // 출력 및 갱신을 위한 선언
    // 각 지점의 탐색 가능 루트 배열 생성
        // 각 지점에서 이동 가능한 루트 저장 및 관리
        // 해당 좌표부터의 탐색이 최초인 경우에, 이를 이용해 depth 계산
        // DFS 함수 실행 시, 계산 작업을 최소화하기 위함
    // 각 지점의 탐색 값 저장 배열 생성
        // 각 지점에서의 최대 depth 저장 및 관리
        // 해당 좌표부터의 탐색이 중복인 경우에, 이를 이용해 depth 계산
        // DFS 함수 실행 시, 계산 작업을 최소화하기 위함
        
    // 탐색 시작 지점 설정
        // 특정 지점이 정해져 있지 않으므로, 모든 지점에서의 탐색 필요
    
    // 탐색 가능 루트 판단 함수
        // 모든 지점을 기준으로, 상하좌우 중 탐색 가능한 루트 판단
        // 이동 가능한 좌표를 탐색 가능 루트 배열에 저장
        
    // DFS 함수
        // 탐색의 재귀 조건
            // 이전 지역과의 정수 비교 후, 방문 여부 판단
        // 모든 지점에서의 탐색 진행
            // 탐색 진행 마다, 최대 탐색 depth 갱신
            // 최대 탐색 depth 갱신 시, 탐색 루트 배열 갱신
                // 배열의 값이 최대인 루트만 남도록 갱신
"""

import sys
#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

#from collections import deque
sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 방향: 상, 하, 좌, 우

n = int(input())
# 입력 처리
bamboo = [list(map(int, input().split())) for _ in range(n)]
# input을 처리하여 가로 행 배열을 생성 후, n번 반복하여 이차원 배열 생성
max_depth = 0
# 최대 탐색 depth 저장 변수 선언
can_move = [[[] for _ in range(n)] for _ in range(n)]
# 각 좌표에서 이동 가능한 루트를 저장 및 관리
path_depth = [[0] * n for _ in range(n)]
# 각 좌표에서의 최대 depth 저장 및 관리

# can_move 계산: 각 좌표에서 상하좌우 중 이동 가능한 좌표 저장
for x in range(n):
    for y in range(n):
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            # 이동 후의 좌표 값
            if 0 <= nx < n and 0 <= ny < n:
                # 이동 후의 좌표 값이 범위 내에 있는 경우
                if bamboo[nx][ny] > bamboo[x][y]:
                    # 이동 후의 좌표 값이 이전 좌표 값보다 큰 경우
                    can_move[x][y].append((nx, ny))

# DFS 함수: can_move와 path_depth를 이용
def dfs(x, y):
    if path_depth[x][y]:
        # 해당 좌표부터의 탐색이 중복인 경우에,
        return path_depth[x][y]
        #이미 저정된 값을 사용
    
    path_depth[x][y] = 1  
    # 각 좌표에서의 시작 구분 (이동 불가의 경우 고려)

    for nx, ny in can_move[x][y]:
        # 해당 좌표부터의 탐색이 최초인 경우, 이미 저정된 값을 사용
        path_depth[x][y] = max(path_depth[x][y], dfs(nx, ny) + 1)
        # 현재 path_depth의 값과 DFS를 통한 재귀 호출 및 탐색 후의 값 중 높은 것을 저장

    return path_depth[x][y]

for i in range(n):
    for j in range(n):
        max_depth = max(max_depth, dfs(i, j))
        # 각 좌표에서의 DFS 탐색 후, 최대 depth라면 갱신

print(max_depth)