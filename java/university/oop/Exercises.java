package university.oop;

import java.util.Scanner;

public class Exercises {
    public static void main() {
        Scanner scanner = new Scanner(System.in);

        // Exercises
        System.out.println(salaryComparison(scanner));

        scanner.close();
    }

    public static double salaryComparison(Scanner scanner) {
        // Slide: 1
        // Page: 52
        final double MIN_SALARY = 1400;
        System.out.println("Qual o seu salario atual? ");
        String input = scanner.nextLine();
        double salary = Double.parseDouble(input);
        double result = salary - MIN_SALARY;
        System.out.println("A diferenca para o salario minimo é: " + result);
        return result;
    }

    public static int[] rand() {
        return rand(3);
    }

    public static int[] rand(int length) {
        int result[] = new int[length];

        for (int i = 0; i < length; i++) {
            result[i] = (int) Math.random() * 100;
        }

        return result;
    }
}