import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static List<Integer>[] tree;
    static int[] parent, depth;
    static boolean[] visited;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine()); // 테스트 케이스 개수

        while (T-- > 0) {
            N = Integer.parseInt(br.readLine()); // 노드 개수
            tree = new ArrayList[N + 1];
            parent = new int[N + 1];
            depth = new int[N + 1];
            visited = new boolean[N + 1];

            for (int i = 1; i <= N; i++) {
                tree[i] = new ArrayList<>();
            }

            // 간선 정보 입력
            for (int i = 0; i < N - 1; i++) {
                st = new StringTokenizer(br.readLine());
                int A = Integer.parseInt(st.nextToken());
                int B = Integer.parseInt(st.nextToken());

                tree[A].add(B);
                parent[B] = A; // B의 부모는 A
            }

            // 루트 찾기 (부모가 없는 노드가 루트)
            int root = 1;
            for (int i = 1; i <= N; i++) {
                if (parent[i] == 0) {
                    root = i;
                    break;
                }
            }

            // DFS를 이용해 각 노드의 깊이 설정
            dfs(root, 0);

            // LCA 구할 두 노드 입력
            st = new StringTokenizer(br.readLine());
            int node1 = Integer.parseInt(st.nextToken());
            int node2 = Integer.parseInt(st.nextToken());

            // LCA 찾기
            System.out.println(findLCA(node1, node2));
        }
    }

    // DFS로 깊이 계산
    static void dfs(int node, int d) {
        depth[node] = d;
        visited[node] = true;

        for (int child : tree[node]) {
            if (!visited[child]) {
                parent[child] = node;
                dfs(child, d + 1);
            }
        }
    }

    // LCA 찾기
    static int findLCA(int u, int v) {
        // 1️⃣ 깊이 맞추기
        while (depth[u] > depth[v]) u = parent[u];
        while (depth[v] > depth[u]) v = parent[v];

        // 2️⃣ 동시에 부모 올리기
        while (u != v) {
            u = parent[u];
            v = parent[v];
        }

        return u;
    }
}
