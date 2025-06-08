# [input]
# 첫째 줄: N, P, Q

# [output]
# An 출력

# [조건]
# 0 <= N <= 10^12
# 2 <= P, Q <= 10^9

# [풀이방법]
# N과 P, Q 최대값을 생각하면 단순이 0부터 N까지 배열 채우는 DP는 불가능
# 딕셔너리를 활용하여 필요한 값만 계산하고 저장하기 (메모이제이션)

import sys
sys.setrecursionlimit(10**7)

sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, P, Q = map(int, input().split())
memo = {0: 1}  # A0는 1이라는 뜻


def A(n):
    if n in memo:
        return memo[n]
    result = A(n//P) + A(n//Q)
    memo[n] = result
    return result


print(A(N))
