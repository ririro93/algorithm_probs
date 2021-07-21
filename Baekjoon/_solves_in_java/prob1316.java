import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Hashtable;
import java.util.StringTokenizer;

public class prob1316 {
    public static void main(String[] args) throws Exception {
        // inputs
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        // init
        int cnt = 0;

        // Test Cases
        for (int tc = 0; tc < N; tc++) {
            // init
            String str = br.readLine();
            Hashtable<Character, Boolean> dict = new Hashtable<>();
            char prev;
            boolean flag = true;

            // exec
            prev = str.charAt(0);
            dict.put(prev, true);
            for (int i = 1; i < str.length(); i++) {
                Boolean bool = dict.get(str.charAt(i));
                // if char already in dict
                if (bool != null) {
                    if (str.charAt(i) == prev) {
                        continue;
                    } else {
                        flag = false;
                        break;
                    }
                // if char not in dict
                } else {
                    prev = str.charAt(i);
                    dict.put(prev, true);
                }
            }

            if (flag) {
                cnt++;
            }
        }

        System.out.println(cnt);

    }
    
}
