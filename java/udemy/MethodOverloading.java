public class MethodOverloading {
    public static void main(String[] args) {
        System.out.println("Hello, World!");

        System.err.print("5000 seconds: ");
        getDuration(5000);
        System.err.print("50000 seconds: ");
        getDuration(50000);
        System.err.print("500000 seconds: ");
        getDuration(500000);
        System.err.print("5000000 seconds: ");
        getDuration(5000000);
        return;
    }

    public static String getDuration(int seconds) {
        int minutes = seconds / 60;
        return getDuration(minutes, seconds % 60);
    }
    public static String getDuration(int minutes, int seconds) {
        int hours = minutes / 60;
        return getDuration(hours, minutes % 60, seconds);
    }
    public static String getDuration(int hours, int minutes, int seconds) {
        int days = hours / 24;
        return getDuration(days, hours % 24, minutes, seconds);
    }
    public static String getDuration(int days, int hours, int minutes, int seconds) {
        String result = days + "d " + hours + "h " + minutes + "m " + seconds + "s";
        System.out.println(result);
        return result;
    }
}
