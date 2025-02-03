public class While {
    public static void main(String[] args) {
        for (int i = 1; i <= 5; i++) {
            System.out.println(i);
        }

        int j = 1;
        while (true) {
            if (j > 5) {
                break;
            }
            System.out.println(j);
            j++;
        }

        int k = 0;
        do {
            System.out.println("Start of the loop k is: '" + k + "'");
            k++;
            System.out.println("End of the loop k is: '" + k + "'");
        } while (k < 10);
    }
}
