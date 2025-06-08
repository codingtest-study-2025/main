# [input]
# 첫째 줄: N
# 둘째 줄: n개의 정수로 이루어진 수열

# [output]
# 첫째 줄: 답

# [조건]
# 1 <= N <= 100,000

# [풀이방법]
# DP 배열을 두 개 사용하여 풀기
# no_del: i번째까지 삭제 없는 최대 연속 합
# one_del: i번쨰까지 삭제 한 번 하는 최대 연속 합

import sys
sys.setrecursionlimit(10**7)

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))


def solution(arr):
    no_del = arr[0]
    one_del = float('-inf')  # 삭제가 발생하기 전에는 선택되지 않도록 음의 무한대로 초기화
    answer = arr[0]

    for x in arr[1:]:
        prev_no_del = no_del
        # 삭제 없이 이어 붙이기 or 새로 시작
        no_del = max(no_del + x, x)
        # 이미 한 번 삭제했을 때 이어 붙이기 or 지금 삭제(=바로 이전까지의 no_del 그대로)
        one_del = max(one_del + x, prev_no_del)
        # 답 갱신
        answer = max(answer, no_del, one_del)

    return answer


print(solution(arr))
