/* input
// 첫 줄: 테스트 케이스 개수 T
    // 각 테스트 케이스
        // 첫 줄: 노드의 수 N (2 ≤ N ≤ 10,000)
        // 다음 N-1줄: 부모 자식 관계 (A B), A는 B의 부모
        // 마지막 줄: 공통 조상을 찾을 두 노드 u v
*/

/* output
    // 각 테스트 케이스마다 두 노드의 가장 가까운 공통 조상 노드 번호 출력
*/

/* process
    // 자료구조
      1. 트리 구성(인접 리스트 형식) : 간선 연결
      2. 자식 입장에서 부모 정보 저장.
      3. DFS로 각 노드의 깊이 저장.
    // 처리
      1. 깊이를 같게 만든 후
      2. 두 노드를 동시에 위로 올려서 공통 조상 찾기
*/

#include <stdio.h>
#include <stdlib.h>

#define MAX 10001


typedef struct Node {
    int child;
    struct Node* next;
} Node;

Node* adj[MAX];  // 인접 행렬 메모리 초과로.. ㅜㅜ 인접 리스트
int parent[MAX];
int depth[MAX];
int visited[MAX];

void addEdge(int from, int to) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->child = to;
    node->next = adj[from];
    adj[from] = node;
}


void dfs(int node, int d) {
    visited[node] = 1;
    depth[node] = d;

    for (Node* cur = adj[node]; cur; cur = cur->next) {
        int next = cur->child;

        if (!visited[next]) {
            parent[next] = node;
            dfs(next, d + 1);
        }
    }
}

int findCommonParent(int a, int b) {
    // 깊이 동일화 : 같은 높이에서 시작해야 '공통 부모'를 찾을 수 있음.
    // (자기 자신이 그 부모일 수도 있음.)
    while (depth[a] > depth[b]) a = parent[a];
    while (depth[b] > depth[a]) b = parent[b];

    // 동시에 위로 올리면서 공통 조상을 찾기
    while (a != b) {
        a = parent[a];
        b = parent[b];
    }
    return a;
}

void init(int N) {
    for (int i = 1; i <= N; i++) {
        parent[i] = 0;
        depth[i] = 0;
        visited[i] = 0;
        adj[i] = NULL;
    }
}

void freeGraph(int N) {
    for (int i = 1; i <= N; i++) {
        Node* cur = adj[i];

        while (cur) {
            Node* tmp = cur;
            cur = cur->next;
            free(tmp);
        }
    }
}


int main() {
    int T;
    scanf("%d", &T);

    while (T--) {
        int N;
        scanf("%d", &N);

        init(N);

        for (int i = 0; i < N - 1; i++) {
            int a, b;
            scanf("%d %d", &a, &b);
            addEdge(a, b);
            parent[b] = a;
        }

        // 루트 노드 찾기 (부모가 없는 노드가 루트)
        int root = 0;
        for (int i = 1; i <= N; i++) {
            if (parent[i] == 0) {
                root = i;
                break;
            }
        }

        // DFS로 깊이 저장
        dfs(root, 0);

        int u, v;
        scanf("%d %d", &u, &v);

        printf("%d\n", findCommonParent(u, v));

        freeGraph(N);
    }

    return 0;
}
