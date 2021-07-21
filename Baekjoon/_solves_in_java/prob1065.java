import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class prob1065 {
    public static void main(String[] args) throws Exception {
        // inputs
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        // init
        int cnt = 0;
        int[] arr = new int[N];
        int[] digits;
        int step;

        // exec
        for (int i = 1; i < arr.length+1; i++) {
            digits = getDigits(i);
            if (digits.length == 1) {
                cnt++;
                continue;
            } else {
                step = digits[0] - digits[1];
                boolean flag = true;
                for (int j = 1; j < digits.length-1; j++) {
                    if (digits[j] - digits[j+1] == step) {
                        continue;
                    } else {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    cnt++;
                }
            }
        }
        System.out.println(cnt);
    }

    public static int[] getDigits(int num) {
        String sb = Integer.toString(num);
        int[] arr = new int[sb.length()];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sb.charAt(i) - '0';
        }
        return arr;
    }   
}