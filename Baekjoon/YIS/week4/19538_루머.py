# [input]
# 첫째 줄: 사람 수 N
# 둘째 줄 ~ N개의 줄: i번 사람의 주변인들의 번호
# 다음 줄: 최초 유포자 수 M
# 마지막 줄: 최초 유포자의 번호들

# [output]
# N개의 정수를 공백 단위로 출력 (t1, t2, t3 ... tN)

# [제한]
# 1 <= N <= 200,000
# 1 <= M <= N
# 주변인 관계 <= 1,000,000

# [참고]
# 주변인이 없는 경우 -1 출력
# 최초 유포자는 0분부터 믿기 시작한다
# 주변인의 절반 이상이 루머를 믿어야 본인도 믿는다

# [풀이방법]
# 주변인 인접 리스트 생성
# 번호별 믿는 시간 리스트 생성 (-1로 초기화)
# 감염까지 남은 카운트 수 리스트 생성
# 최초 유포자를 큐에 넣기
# BFS 수행
#   - 주변인들에 대해
#       - 감염 카운트 -1 하고
#       - 아직 감염되지 않았고 감염 카운트가 0이면
#           - 큐에 주변인 넣고 answer 시간 갱신

import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]
q = deque()

for i in range(1, N + 1):
    line = list(map(int, input().split()))
    for neighbor in line:
        graph[i].append(neighbor)

M = int(input())

first_members = list(map(int, input().split()))

answer = [-1] * (N + 1)

turn = [0] * (N + 1)

for first_member in first_members:
    q.append(first_member)
    answer[first_member] = 0

for i in range(1, N + 1):
    turn[i] = (len(graph[i])) // 2

while q:
    current = q.popleft()
    for next in graph[current]:
        if next == 0:
            break
        turn[next] -= 1
        if answer[next] == -1 and turn[next] <= 0:
            q.append(next)
            answer[next] = answer[current] + 1
            print('answer', next, answer, current, answer[current])

print(answer)
