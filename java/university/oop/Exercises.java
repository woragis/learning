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
}