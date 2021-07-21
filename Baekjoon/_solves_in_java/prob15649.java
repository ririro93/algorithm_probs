import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class prob15649 {
    static int N, M;
    static boolean[] visited;

    public static void main(String[] args) throws Exception {
        // inputs
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        // init
        visited = new boolean[N+1];

        // exec
        printPermus(0, "");
    }

    static void printPermus(int depth, String str) {
        if (depth == M) {
            System.out.println(str);
            return;
        }

        for (int i = 1; i < N+1; i++) {
            if (!visited[i]) {
                visited[i] = true;
                printPermus(depth+1, str+Integer.toString(i)+" ");
                visited[i] = false;
            }
        }
    }
}