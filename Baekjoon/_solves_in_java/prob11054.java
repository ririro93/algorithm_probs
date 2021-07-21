import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class prob11054 {
    static int[] arr, inc, dec;
    static int N, result;
    public static void main(String[] args) throws Exception {
        // inputs
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = Arrays.stream(br.readLine().split(" ")).mapToInt(str -> Integer.parseInt(str)).toArray();

        // init
        inc = new int[N];
        dec = new int[N];
        result = 0;

        // exec
        for (int i = 0; i < N; i++) {
            getInc(i);
            getDec(N-1-i);
        }

        for (int i = 0; i < N; i++) {
            result = Math.max(result, inc[i] + dec[i] - 1);
        }

        System.out.println(result);
    }

    static void getInc(int idx) {
        inc[idx] = 1;
        for (int i = idx-1; i >= 0; i--) {
            if (arr[i] < arr[idx]) {
                inc[idx] = Math.max(inc[idx], inc[i]+1);
            }
        }
    }

    static void getDec(int idx) {
        dec[idx] = 1;
        for (int i = idx+1; i <= N-1; i++) {
            if (arr[i] < arr[idx]) {
                dec[idx] = Math.max(dec[idx], dec[i]+1);
            }
        }
    }
}
