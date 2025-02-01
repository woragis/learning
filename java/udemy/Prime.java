
public class Prime {
    static int START = 0;
    static int END = 1000;

    public static void main(String[] args) {
        int count = 0;
        for (int i = START; i <= END; i++) {
            if (isPrime(i)) {
                System.out.println(i + " is prime!");
                count++;
            }
        }
        System.out.println("Total prime numbers found in between: '" + START + "'' and '" + END + "' is: " + count);

    }

    public static boolean isPrime(int number) {
        if (number <= 2) {
            return number == 2;
        }

        for (int i = 2; i <= number / 2; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}
