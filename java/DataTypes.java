public class DataTypes {
    
    // Alphabetic DataTypes
    public static void charDataType() {
        byte charBytes = Character.BYTES, charSize = Character.SIZE, charMin = Character.MIN_VALUE;
        int charMax = Character.MAX_VALUE;
        System.out.println("\n---------Char---------");
        System.out.println("Bytes: " + charBytes);
        System.out.println("Size: " + charSize);
        System.out.println("Range value: " + charMin + " to " + charMax + ")");
        System.out.println("----------------------");
    }
    
    // Numeric Data Types
    public static void byteDataType() {
        byte byteBytes = Byte.BYTES, byteSize = Byte.SIZE, byteMin = Byte.MIN_VALUE, byteMax = Byte.MAX_VALUE;
        System.out.println("\n---------Byte---------");
        System.out.println("Bytes: " + byteBytes);
        System.out.println("Size: " + byteSize);
        System.out.println("Range value: (" + byteMin + " to " + byteMax + ")");
        System.out.println("----------------------");
    }

    public static void shortDataType() {
        byte shortBytes = Short.BYTES, shortSize = Short.SIZE;
        short shortMin = Short.MIN_VALUE, shortMax = Short.MAX_VALUE;
        System.out.println("\n---------Short--------");
        System.out.println("Bytes: " + shortBytes);
        System.out.println("Size: " + shortSize);
        System.out.println("Range value: (" + shortMin + " to " + shortMax + ")");
        System.out.println("----------------------");
    }

    public static void intDataType() {
        byte intBytes = Integer.BYTES, intSize = Integer.SIZE;
        int intMin = Integer.MIN_VALUE, intMax = Integer.MAX_VALUE;
        System.out.println("\n--------Integer-------");
        System.out.println("Bytes: " + intBytes);
        System.out.println("Size: " + intSize);
        System.out.println("Range value: (" + intMin + " to " + intMax + ")");
        System.out.println("----------------------");
    }

    public static void longDataType() {
        byte longBytes = Long.BYTES, longSize = Long.SIZE;
        long longMin = Long.MIN_VALUE, longMax = Long.MAX_VALUE;
        System.out.println("\n---------Long---------");
        System.out.println("Bytes: " + longBytes);
        System.out.println("Size: " + longSize);
        System.out.println("Range value: (" + longMin + " to " + longMax + ")");
        System.out.println("----------------------");
    }

    // Floating Numeric DataTypes
    public static void floatDataType() {
        byte floatBytes = Float.BYTES, floatSize = Float.SIZE;
        float floatMin = Float.MIN_VALUE, floatMax = Float.MAX_VALUE;
        System.out.println("\n---------Float--------");
        System.out.println("Bytes: " + floatBytes);
        System.out.println("Size: " + floatSize);
        System.out.println("Range value: (" + floatMin + " to " + floatMax + ")");
        System.out.println("----------------------");
    }

    public static void doubleDataType() {
        byte doubleBytes = Double.BYTES, doubleSize = Double.SIZE;
        double doubleMin = Double.MIN_VALUE, doubleMax = Double.MAX_VALUE;
        System.out.println("\n---------Float--------");
        System.out.println("Bytes: " + doubleBytes);
        System.out.println("Size: " + doubleSize);
        System.out.println("Range value: (" + doubleMin + " to " + doubleMax + ")");
        System.out.println("----------------------");
    }
}
