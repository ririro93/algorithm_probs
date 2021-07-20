public class test {
    public static void main(String[] args) {
        int a = 3123123;
        char[] b = Integer.toString(a).toCharArray();
        for (int i = 0; i < b.length; i++) {
            System.out.println(b[i] - '0');
        }
    }
}
