/* input
 // 첫 줄: 공간 크기 N (2 ≤ N ≤ 20)
 // 다음 N줄: 공간의 상태 (0: 빈 칸, 1~6: 물고기 크기, 9: 아기상어 위치)
*/

/* output
 // 아기 상어가 도움 요청 없이 물고기를 잡아먹을 수 있는 총 시간 출력
*/

/* process
 - 공간 정보를 2차원 배열에 저장
 - 아기 상어의 위치를 찾고, 크기=2, 먹은 물고기 수=0으로 시작
 1. BFS를 통해 가장 가까운 먹을 수 있는 물고기 탐색
   - 거리가 가장 짧은 물고기
 2. 여러 개면, 가장 위, 가장 왼쪽
 3. 먹을 때마다 시간 누적, 물고기 수 증가
 4. 먹은 수 == 상어 크기이면, 상어 크기 +1
 5. 더 이상 먹을 물고기가 없으면 종료
*/



#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 20
#define INF 1e9

typedef struct {
    int x, y, dist;
} Shark;

int n;
int map[MAX][MAX];
int visited[MAX][MAX];
int dx[4] = {-1, 0, 0, 1}; //  (우선순위 주의)
int dy[4] = {0, -1, 1, 0};

FILE* input;

Shark bfs(int sx, int sy, int size) {
    Shark result = { -1, -1, INF };
    Shark queue[MAX * MAX];
    int front = 0, rear = 0;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            visited[i][j] = 0;

    visited[sx][sy] = 1;
    queue[rear++] = (Shark){sx, sy, 0};

    while (front < rear) {
        Shark cur = queue[front++];

        // 먹을 수 있는 물고기 발견
        if (map[cur.x][cur.y] > 0 && map[cur.x][cur.y] < size) {
            if (cur.dist < result.dist ||
                (cur.dist == result.dist && (cur.x < result.x || (cur.x == result.x && cur.y < result.y)))) {
                result = cur;
            }
        }

        for (int dir = 0; dir < 4; dir++) {
            int nx = cur.x + dx[dir];
            int ny = cur.y + dy[dir];

            if (nx < 0 || ny < 0 || nx >= n || ny >= n)
                continue;
            if (visited[nx][ny])
                continue;
            if (map[nx][ny] > size) // 큰 물고기가 있는 칸은 못 지나감
                continue;

            visited[nx][ny] = 1;
            queue[rear++] = (Shark){nx, ny, cur.dist + 1};
        }
    }

    return result;
}

int main(int argc, char* argv[]) {
    input = stdin;

    if (argc == 3 && strcmp(argv[1], "-f") == 0) {
        FILE* file = fopen(argv[2], "r");
        if (!file) {
            fprintf(stderr, "파일 열기 실패: %s\n", argv[2]);
            return 1;
        }
        input = file;
    }

    fscanf(input, "%d", &n);

    int sx, sy; 

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            fscanf(input, "%d", &map[i][j]);
            if (map[i][j] == 9) {
                sx = i;
                sy = j;
                map[i][j] = 0; // 초기 상어 위치는 빈칸
            }
        }
    }

    int time = 0;
    int size = 2;
    int eat = 0;

    while (1) {
        Shark target = bfs(sx, sy, size);

        if (target.dist == INF)
            break; 

        time += target.dist;
        sx = target.x;
        sy = target.y;

        map[sx][sy] = 0;
        eat++;

        if (eat == size) {
            size++;
            eat = 0;
        }
    }

    printf("%d\n", time);

    if (input != stdin) {
        fclose(input);
    }

    return 0;
}

