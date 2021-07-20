public class prob4673 {
    public static void main(String[] args) throws Exception {
        // inputs

        
        // init
        boolean[] arr = new boolean[10001];
        for (int i=0; i<10001; i++) {
            arr[i] = true;
        }
        int sum;

        // exec
        for (int i=1; i<10001; i++) {
            sum = i;
            char[] b = Integer.toString(i).toCharArray();
            
            for (int j = 0; j < b.length; j++) {
                sum += b[j] - '0';
            }

            if (sum < 10001) {
                arr[sum] = false;
            }
            
        }

        for (int i = 1; i < 10001; i++) {
            if (arr[i]) {
                System.out.println(i);
            }
        }
    }
    
}
