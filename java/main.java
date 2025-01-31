public class main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        intDataType();
        byteDataType();
        shortDataType();
        longDataType();
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

    public static void longDataType() {
        long longMin = Long.MIN_VALUE;
        long longMax = Long.MAX_VALUE;
        long longSize = Long.SIZE;
        long longByte = Long.BYTES;
        System.out.println("Min Long number: " + longMin);
        System.out.println("Max Long number: " + longMax);
        System.out.println("Long Size: " + longSize);
        System.out.println("Long Bytes: " + longByte);
    }

    public static void byteDataType() {
        byte byteMin = Byte.MIN_VALUE;
        byte byteMax = Byte.MAX_VALUE;
        byte byteSize = Byte.SIZE;
        byte byteByte = Byte.BYTES;
        System.out.println("Min Byte number: " + byteMin);
        System.out.println("Max Byte number: " + byteMax);
        System.out.println("Byte Size: " + byteSize);
        System.out.println("Byte Bytes: " + byteByte);
    }

    public static void shortDataType() {
        short shortMin = Short.MIN_VALUE;
        short shortMax = Short.MAX_VALUE;
        short shortSize = Short.SIZE;
        short shortByte = Short.BYTES;
        System.out.println("Min Short number: " + shortMin);
        System.out.println("Max Short number: " + shortMax);
        System.out.println("Short Size: " + shortSize);
        System.out.println("Short Bytes: " + shortByte);
    }
}