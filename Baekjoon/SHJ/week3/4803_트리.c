/* input
    // 각 테스트 케이스
        // 첫 줄: 정점 수 n (1 ≤ n ≤ 500), 간선 수 m
        // 다음 m줄: 정점 간 간선 정보 (무방향 간선) u v
    // 입력의 마지막 줄은 "0 0"으로 종료
*/

/* output
    // 트리가 없으면       ->  Case X: No trees.
    // 트리 하나면         ->  Case X: There is one tree.
    // 트리 여러 개면      ->  Case X: A forest of T trees.
*/

/* process
 *  무방향을 표현하기 위한 간선과 실제로 지나가야 하는 간선을 구분해야됨. (key)
    // 1. 인접 행렬 구성
    // 2. DFS로 연결된 정점들을 방문하되, 재방문한다는 의미 -> 사이클
        // - 다만, 무방향이라서 각 측에서 재방문을 할 가능성이 있으므로, 구분해야할 로직이 필요함!
    // 3. 사이클이 안생긴 서브트리에 대해서만 카운트
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 501

int parent[MAX];
int visited[MAX];
int adj[MAX][MAX];
int stack[MAX];
int n, m;
int caseNum = 1;
FILE* input = NULL;

int solve() {
    memset(adj, 0, sizeof(adj));
    for (int i = 0; i < MAX; ++i) parent[i] = i;

    if (fscanf(input, "%d %d", &n, &m) != 2 || (n == 0 && m == 0)) {
        return 0;
    }

    for (int i = 0; i < m; ++i) {
        int u, v;
        if (fscanf(input, "%d %d", &u, &v) != 2) return 0;
        adj[u][v] = adj[v][u] =1;
    }

    memset(visited, 0, sizeof(visited));
    int treeCount = 0;

    for (int i = 1; i <= n; ++i) {
        if (visited[i]) continue;
        int hasCycle=0;
        int top = 0;
        stack[top++] = i;
        visited[i] = 1;

        while (top > 0) {
            int cur = stack[--top];
            for (int next = 1; next <= n; ++next) {
                if (adj[cur][next] ) {
                   adj[cur][next] = adj[next][cur]= 0; // 같은 간선은 여러번 주어지지 않기 때문에 마킹
                   
                    if ( !visited[next] ) { 
                        visited[next] = 1;
                        stack[top++] = next;  
                   } else {
                       hasCycle =1; 
                   }
                }
            }
        }
        if(!hasCycle) treeCount++;
    }
    
    printf("Case %d: ", caseNum++);
    if (treeCount == 0) puts("No trees.");
    else if (treeCount == 1) puts("There is one tree.");
    else printf("A forest of %d trees.\n", treeCount);

    return 1;
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

    while (solve());

    if (input != stdin) fclose(input);
    return 0;
}



