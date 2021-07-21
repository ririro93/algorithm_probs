import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class prob10870 {
    public static void main(String[] args) throws Exception {
        // inputs
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        // init
        
        // exec
        int result = fibo(N);
        System.out.println(result);
    }

    public static int fibo(int num) {
        if (num == 0) {
            return 0;
        } else if (num == 1) {
            return 1;
        } else {
            return fibo(num-1) + fibo(num-2);
        }

    }
}
