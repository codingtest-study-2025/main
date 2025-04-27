/* input
  // 첫 줄: 대나무 숲의 크기 n (1 ≤ n ≤ 500)
  // 다음 n줄: 대나무 숲의 정보 (공백으로 구분된 각 칸의 대나무 양)
*/

/* output
  // 판다가 이동할 수 있는 칸의 수의 최댓값 출력
*/

/* process
  -  n × n 대나무 숲 정보를 2차원 배열에 저장
  - 판다 이동 조건: 현재 칸보다 대나무가 많은 칸으로 상, 하, 좌, 우 이동 가능
  1. 각 칸을 시작점으로, 최대 몇 칸을 이동할 수 있는지 계산
  2-1. 이동할 수 있으면 길이 +1 하면서 이동
  2-2. 이동할 수 없으면 종료
  3. DFS를 이용하여 탐색, 메모이제이션(DP)으로 최적화
  4. 이미 계산한 칸은 DP 배열 값을 바로 사용
  5. 모든 칸을 시작점으로 DFS를 돌려서, 가장 큰 이동 칸 수를 찾기
*/

#include <stdio.h>
#include <string.h>

#define MAX 500

int n;
int forest[MAX][MAX];
int dp[MAX][MAX];

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int dfs(int x, int y) {
    if (dp[x][y] != 0)
        return dp[x][y];

    dp[x][y] = 1; // 자기 자신만 방문했을 때 기본값 1

    for (int dir = 0; dir < 4; dir++) {
        int nx = x + dx[dir];
        int ny = y + dy[dir];

        if (nx < 0 || ny < 0 || nx >= n || ny >= n)
            continue;

        if (forest[nx][ny] > forest[x][y]) {
            int next = dfs(nx, ny);
            if (dp[x][y] < next + 1)
                dp[x][y] = next + 1;
        }
    }

    return dp[x][y];
}

int main(int argc, char* argv[]) {
    FILE* input = stdin;

    if (argc == 3 && strcmp(argv[1], "-f") == 0) {
        FILE* file = fopen(argv[2], "r");
        if (!file) {
            fprintf(stderr, "파일 열기 실패: %s\n", argv[2]);
            return 1;
        }
        input = file;
    }

    fscanf(input, "%d", &n);

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            fscanf(input, "%d", &forest[i][j]);

    int result = 0;

    // 모든 칸을 출발점으로 시도
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            int temp = dfs(i, j);
            if (result < temp)
                result = temp;
        }

    printf("%d\n", result);

    if (input != stdin) {
        fclose(input);
    }

    return 0;
}



