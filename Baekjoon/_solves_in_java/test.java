import java.util.Arrays;

public class test {
    static int[] arr;
    public static void main(String[] args) {
        // int[] arr = new int[10];
        arr = new int[10];
        for (int i = 0; i < 10; i++) {
            arr[i] = i;
        }
        System.out.println(Arrays.toString(arr));
    }
}
