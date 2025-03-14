import java.util.Scanner;

import university.oop.Exercises;

public class Main {
    public static void main(String[] args) {
        // System.out.println("Hello, World!\n");
        // System.out.println("Data types properties:");
        // DataTypes.charDataType();
        // DataTypes.byteDataType();
        // DataTypes.shortDataType();
        // DataTypes.intDataType();
        // DataTypes.longDataType();
        // DataTypes.floatDataType();
        // DataTypes.doubleDataType();

        // Exercises.weightOnPlanets();
        // Exercises.jobPromotion();
        Scanner scanner = new Scanner(System.in);

        Exercises.taxCalculator(scanner);

        scanner.close();
    }

}
