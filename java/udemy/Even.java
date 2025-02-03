public class Even {
    public static void main(String[] args) {
        int start = 0;
        int end = 20;
        int i = start;
        while (i < end) {
            i++;
            if (!isEven(i)) {
                continue;
            }
            System.out.println("Even number: " + i);
        }
    }

    public static boolean isEven(int number) {
        return number % 2 == 0;
    }
}
