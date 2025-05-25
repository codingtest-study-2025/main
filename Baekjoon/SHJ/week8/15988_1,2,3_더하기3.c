/* input
 // 첫 줄: 정수 T (테스트 케이스 개수)
 // 다음 T줄: 정수 n (1 ≤ n ≤ 1,000,000)
*/

/* output
 // 각 테스트 케이스마다
 // n을 1, 2, 3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지 출력
*/

/* process
 - 점화식: dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
 - 의미: n을 만들기 위해 마지막에 1, 2, 3을 붙이는 경우의 수를 더함
 - 초기값:
   dp[0] = 1   // 아무것도 선택하지 않는 경우
   dp[1] = 1   // [1]
   dp[2] = 2   // [1+1], [2]
   dp[3] = 4   // [1+1+1], [1+2], [2+1], [3]

 - 모든 테스트 케이스 중 가장 큰 n까지 dp를 미리 계산
 - 각 테스트 케이스마다 dp[n] 출력
 - 모든 연산은 1,000,000,009로 나눈 나머지로 처리
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MOD 1000000009
#define MAX 1000001

long long dp[MAX];

void precompute() {
    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;

    for (int i = 4; i < MAX; i++) {
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD;
    }
}

int main(int argc, char* argv[]) {
    FILE* input = stdin;

    // 파일 입력 옵션 처리
    if (argc == 3 && strcmp(argv[1], "-f") == 0) {
        FILE* file = fopen(argv[2], "r");
        if (!file) {
            fprintf(stderr, "파일 열기 실패: %s\n", argv[2]);
            return 1;
        }
        input = file;
    }

    int T, n;
    precompute();

    fscanf(input, "%d", &T);
    while (T--) {
        fscanf(input, "%d", &n);
        printf("%lld\n", dp[n]);
    }

    if (input != stdin) {
        fclose(input);
    }

    return 0;
}

