public class Flow {
    public static void main(String[] args) {
        int myVal = 4;
        oldSwitch(myVal);
    }

    public static void oldSwitch(int val) {
        switch (val) {
            // Switch cases can be used for:
            // byte, short, int, char
            // String
            // Enum
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

    // public static void enhancedSwitch(int val) {
    // Not Working with my Java version
    // switch (val) {
    // // Switch cases can be used for:
    // // byte, short, int, char
    // // String
    // // Enum
    // case 1 -> System.out.println("Value was 1");
    // case 2 -> System.out.println("Value was 2");
    // case 3, case 4, case 5 -> {
    // System.out.println("Value is probrably 3, 4 or 5");
    // }
    // default -> System.out.println("Value was something i didont expect");
    // }
    // return switch (val) {
    // // Switch cases can be used for:
    // // byte, short, int, char
    // // String
    // // Enum
    // case 1 -> 3;
    // case 2 -> 4;
    // case 3, case 4, case 5 -> {
    // System.out.println("Value is probrably 3, 4 or 5");
    // yield 5;
    // }
    // default -> 6;
    // }
    // }

}