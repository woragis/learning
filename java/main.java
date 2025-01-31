public class main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        intDataType();
    }

    public static void intDataType() {
        int intMin = Integer.MIN_VALUE;
        int intMax = Integer.MAX_VALUE;
        int intSize = Integer.SIZE;
        int intByte = Integer.BYTES;
        System.out.println("Min Integer number: " + intMin);
        System.out.println("Max Integer number: " + intMax);
        System.out.println("Integer Size: " + intSize);
        System.out.println("Integer Bytes: " + intByte);
    }
}