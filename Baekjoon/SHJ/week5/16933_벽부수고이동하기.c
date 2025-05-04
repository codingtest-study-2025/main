/* input
 // 첫 줄: 세 개의 정수 N(행), M(열), K(벽 부수기 가능 횟수)
 // 다음 N줄: M개의 숫자 (0: 이동 가능, 1: 벽)
 // (1, 1)과 (N, M)은 항상 0
*/

/* output
 // (1, 1)에서 (N, M)까지 최단 거리 (칸 수)
 // 이동이 불가능할 경우 -1 출력
*/

/* process
 - 맵 정보를 2차원 배열로 저장
 - 상태 관리
   1. 현재 좌표 (x, y)
   2. 현재까지 이동한 거리
   3. 벽을 부순 횟수 (0 ~ K)
   4. 현재 시간이 낮인지 밤인지 (낮:0, 밤:1)

 - BFS 탐색 시 조건
   1. 0인 칸 : 언제든 이동 가능
   2. 1인 칸(벽) : 벽을 부순 횟수 < K && 현재가 낮이면 부수고 이동
   3. 밤인데 벽 : 이동하지 않고 제자리에서 머물러서 낮을 기다림. (칸 수 +1)

 ! 같은 좌표라도 [벽 부순 횟수][낮/밤] 상태가 다르면 다른 상태로 간주
*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 1001

typedef struct {
    int x, y, dist;
    int wallCount;
    int isDay;
} State;

int n, m, k;
int map[MAX][MAX];
int visited[MAX][MAX][11][2]; // [x][y][벽 부순 횟수][낮/밤]

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

State queue[MAX * MAX * 11 * 2];
int front = 0, rear = 0;

void enqueue(State s) { queue[rear++] = s; }
State dequeue() { return queue[front++]; }
int isEmpty() { return front == rear; }

int bfs() {
    State start = {0, 0, 1, 0, 1};
    visited[0][0][0][1] = 1;
    enqueue(start);

    while (!isEmpty()) {
        State cur = dequeue();

        if (cur.x == n - 1 && cur.y == m - 1) {
            return cur.dist;
        }

        for (int dir = 0; dir < 4; dir++) {
            int nx = cur.x + dx[dir];
            int ny = cur.y + dy[dir];
            int nextDay = !cur.isDay;

            if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;

            if (map[nx][ny] == 0 && !visited[nx][ny][cur.wallCount][nextDay]) {
                visited[nx][ny][cur.wallCount][nextDay] = 1;
                enqueue((State){nx, ny, cur.dist + 1, cur.wallCount, nextDay});
            } // 움직일 수 없는데, 낮이고, 벽을 부술 수 있을 때
            else if (map[nx][ny] == 1 && cur.isDay == 1 && cur.wallCount < k &&
                     !visited[nx][ny][cur.wallCount + 1][nextDay]) {
                visited[nx][ny][cur.wallCount + 1][nextDay] = 1;
                enqueue((State){nx, ny, cur.dist + 1, cur.wallCount + 1, nextDay});
            }
        }

        int nextDay = !cur.isDay;
        if (!visited[cur.x][cur.y][cur.wallCount][nextDay]) {
            visited[cur.x][cur.y][cur.wallCount][nextDay] = 1;
            enqueue((State){cur.x, cur.y, cur.dist + 1, cur.wallCount, nextDay});
        }
    }

    return -1;
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

    fscanf(input, "%d %d %d", &n, &m, &k);
    for (int i = 0; i < n; i++) {
        char row[MAX];
        fscanf(input, "%s", row);
        for (int j = 0; j < m; j++) {
            map[i][j] = row[j] - '0';
        }
    }

    printf("%d\n", bfs());
    return 0;
}


