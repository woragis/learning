import java.util.Scanner;

public class Flow {
    public static void main(String[] args) {
        // Switch cases can be used for:
        // byte, short, int, char
        // String
        // Enum

        try {
            String myName = new String("Jezreel");
            System.out.println(myName);
        } catch (Exception e) {
            System.err.println(e);
        } finally {
            System.out.println("End");
            System.exit(0);
        }
        int myVal = 4;
        oldSwitch(myVal);
        System.out.println("Month 5 is in the : " + monthQuarter(8) + " quarter of the year");
    }

    public static void scanStdin() {
        Scanner scanner = new Scanner(System.in);
        scanner.nextLine();
        scanner.close();
    }

    public static void oldSwitch(int val) {
        switch (val) {
            case 1:
                System.out.println("Value was 1");
                break;
            case 2:
                System.out.println("Value was 2");
                break;
            case 3:
            case 4:
            case 5:
                System.out.println("Value is probrably 3, 4 or 5");
                break;
            default:
                System.out.println("Value was something i didont expect");
                break;
        }
    }

    public static void enhancedSwitch(int val) {
        switch (val) {
            case 1 -> System.out.println("Value was 1");
            case 2 -> System.out.println("Value was 2");
            case 3, 4, 5 -> {
                System.out.println("Value is probrably 3, 4 or 5");
            }
            default -> System.out.println("Value was something i didont expect");
        }
    }

    public static int monthQuarter(int month) {
        return switch (month) {
            case 1, 2, 3 -> 1;
            case 4, 5, 6 -> 2;
            case 7, 8, 9 -> 3;
            case 10, 11, 12 -> 4;
            default -> {
                System.out.println("Month not valid");
                yield 0;
            }
        };
    }

}