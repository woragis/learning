public class Sum {
    static int START = 0;
    static int END = 1000;

    public static void main(String[] args) {
        int total = 0;
        for (int i = START; i <= END; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                total = sum(total, i);
                System.out.println("Number " + i + " is divisible by 3 and 5!");
            }
        }
        System.out.println(
                "Total sum of numbers divisible by 3 and 5 in range '" + START + "' to '" + END + "' is: " + total);

    }

    public static int sum(int total, int value) {
        return total + value;
    }

}
