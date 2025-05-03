""" 
input
    N개의 마을에 각 1명의 학생
        // N개의 마을 당 한명 = N명의 학생
    X = 파티 장소
    M = 마을 간 단방향 도로
    i번째 도로를 지나는 시간 = Ti
    이동 후 복귀 + 최단 시간 + 오가는 경로 다를 수 있음음

    첫째 줄: N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 10,000), X
    두번째 ~ M+1번째 줄: i번째 도로의 시작점, 끝점, 도로를 지나는데 필요한 소요시간 Ti

output
    첫째 줄: N명의 학생들 중 가장 높은 Ti 출력

process
    시간 제한 1초, 메모리 제한 128MB 고려
    N = 4
    M = 8
    X = 2

    1 2 4
    1 3 2
    1 4 7
    2 1 1
    2 3 5
    3 1 2
    3 4 4
    4 2 3
    
    1 = 2, 3, 4
    2 = 1, 3
    3 = 1, 4
    4 = 2

    X = 2

    학생 1
        마을 1 -> [X 2] = 4
        [X 2] -> 마을 1 = 1
        마을 1 -> [X 2] -> 마을 1 = 5 [0]
    학생 2
        마을 2 -> [X 2] = 0
        [X 2] -> 마을 2 = 0
        마을 2 -> [X 2] -> 마을 2 = 0 [0]
    학생 3
        마을 3 -> 마을 1 = 2
        마을 1 -> [X 2] = 4
        마을 3 -> 마을 1 -> [X 2] = 6 [0]

        마을 3 -> 마을 4 = 4
        마을 4 -> [X 2] = 3
        마을 3 -> 마을 4 -> [X 2] = 7 [X]
        
        [X 2] -> 마을 3 = 5 [X]

        [X 2] -> 마을 1 = 1
        마을 1 -> 마을 3 = 2
        [X 2] -> 마을 1 -> 마을 3 = 3 [0]

        마을 3 -> 마을 1 -> [X 2] -> 마을 1 -> 마을 3 = 9
    학생 4
        마을 4 -> [X 2] = 3

        [X 2] -> 마을 1 = 1
        마을 1 -> 마을 4 = 7
        [X 2] -> 마을 1 -> 마을 4 = 8 [X]

        [X 2] -> 마을 1 = 1
        마을 1 -> 마을 3 = 2
        마을 3 -> 마을 4 = 4
        [X 2] -> 마을 1 -> 마을 3 -> 마을 4 = 7 [0]

        [X 2] -> 마을 3 = 5
        마을 3 -> 마을 4 = 4
        [X 2] -> 마을 3 -> 마을 4 = 9 [X]

        [X 2] -> 마을 3 = 5
        마을 3 -> 마을 1 = 2
        마을 1 -> 마을 4 = 7
        [X 2] -> 마을 3 -> 마을 1 -> 마을 4 = 14 [X]

        마을 4 -> [X 2] -> 마을 1 -> 마을 3 -> 마을 4 = 10

    사용 변수
        N, M, X
        start, end, time

    첫째 줄 input 처리
        N, M, X
    두번째 ~ M+1번째 줄 input 처리
        start, end, time

    마을의 이동 가능 배열
        index = 마을 번호 start i
        value = 이동 가능 마을 end 번호, 이동 시간 time
    되돌아오는 마을의 이동 배열 = 마을의 이동 가능 역배열
        index = 마을 번호 end i
        value = 이동 가능 마을 start 번호, 이동 시간 time

    다익스트라 함수
        탐색 시작 마을 = i, X
        거리 배열
            index = 마을 번호
            value = 거리 값
            초기 value = N 최대치 x M 최대치 x Ti 최대치

        탐색 시작
            time = 0, 마을 = i, X
            최대 이동 시간과 정/역배열을 통해 탐색

            거리 배열의 값과 현재 time 비교
                현재 time이 더 적은 경우 진행, 크면 스킵
            각 배열을 통해 다음 마을 및 이동 시간 갱신
            아직 안 간 경로라면, 거리 배열 값 갱신 및 탐색 큐에 추가
    
    i, X 모두 시작점으로 함수 탐색
"""

import sys

#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

import heapq
#from collections import deque
#sys.setrecursionlimit(10**6)

N, M, X = map(int, input().split())
# 첫째 줄 input 처리

move_route = [[] for _ in range(N + 1)]
reverse_move_route = [[] for _ in range(N + 1)]
# 이동 가능 정/역배열

for _ in range(M):
    start, end, time = map(int, input().split())
    move_route[start].append((end, time))
    # index = 마을 번호 start i
    # value = 이동 가능 마을 end 번호, 이동 시간 time
    reverse_move_route[end].append((start, time))
    # index = 마을 번호 end i
    # value = 이동 가능 마을 start 번호, 이동 시간 time

def dijkstra(start, route):
    # i, X에서 시작하고, route에 따라 탐색
    max_time = 100000
    # 최대 이동 시간 = N=1000, Ti=100 → (N-1)*Ti = 999*100 = 99900
    time = [max_time] * (N + 1)
    # 이동 시간 배열 초기화
    time[start] = 0
    # 시작 마을 이동 시간 0
    pq = [(0, start)]
    # 탐색 큐 초기화

    while pq:
        current_time, current = heapq.heappop(pq)
        # 현재 이동 시간 및 마을 번호

        if current_time <= time[current]:
            # 현재 이동 시간이 더 적은 경우
            for next_node, move_time in route[current]:
                # 정/역배열에 따른 다음 마을 및 이동 시간
                new_time = current_time + move_time
                # 다음 마을 이동 시간
                if time[next_node] > new_time:
                    # 다음 마을 이동 시간이 더 적은 경우
                    time[next_node] = new_time
                    # 이동 시간 갱신
                    heapq.heappush(pq, (new_time, next_node))
                    # 탐색 큐에 추가
    return time

i_to_X = dijkstra(X, reverse_move_route)  
# 각 마을 i에서 X까지 (i → X) = X에서 각 마을로 가는 최단 시간
X_to_i = dijkstra(X, move_route)          
# X에서 각 마을 i까지 (X → i) = 각 마을에서 X로 가는 최단 시간

total_time = 0
for i in range(1, N + 1):
    total = i_to_X[i] + X_to_i[i]
    if total > total_time:
        total_time = total

print(total_time)