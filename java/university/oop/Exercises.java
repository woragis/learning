package university.oop;

import java.util.ArrayList;
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
        double result = Math.abs(salary - MIN_SALARY);
        if (salary < MIN_SALARY) {
            System.out.println("Voce ganha: '" + result + "' a menos que o salario minimo");
        } else if (salary > MIN_SALARY) {
            System.out.println("Voce ganha: '" + result + "' a mais que o salario minimo");
        } else {
            System.out.println("Voce ganha um salario minimo");
        }
        return result;
    }

    public static int[] rand() {
        // Slide: 2
        // Page: 37
        return rand(3);
    }

    public static int[] rand(int length) {
        // Slide: 2
        // Page: 37
        int result[] = new int[length];

        for (int i = 0; i < length; i++) {
            result[i] = (int) Math.random() * 100;
        }

        return result;
    }

    public static double graphic(Scanner scanner) {
        // Slide: 2
        // Page: 40
        int x1, x2, y1, y2;
        System.out.println("First coordinate");
        System.out.print("X: ");
        x1 = Integer.parseInt(scanner.nextLine());
        System.out.print("Y: ");
        y1 = Integer.parseInt(scanner.nextLine());

        System.out.println("Second coordinate");
        System.out.print("X: ");
        x2 = Integer.parseInt(scanner.nextLine());
        System.out.print("Y: ");
        y2 = Integer.parseInt(scanner.nextLine());

        return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
    }

    public static void weightOnPlanets(Scanner scanner) {
        // Slide: 2
        // Page: 41
        // Gravity and Weight exercise
        String input, name;
        double weight;

        System.out.println("Digite seu nome: ");
        input = scanner.nextLine();
        name = input;

        System.out.println("Digite seu peso: ");
        input = scanner.nextLine();
        weight = Double.parseDouble(input);

        User user = new User(name, weight);

        ArrayList<Planet> myPlanets = new ArrayList<Planet>();
        myPlanets.add(new Planet("mercury", 0.37));
        myPlanets.add(new Planet("venus", 0.88));
        myPlanets.add(new Planet("mars", 0.38));
        myPlanets.add(new Planet("jupiter", 2.64));
        myPlanets.add(new Planet("satturn", 1.15));
        myPlanets.add(new Planet("uranium", 1.17));

        int count = myPlanets.size();

        System.out.println(user);

        // Iterate through all Planets
        for (int i = 0; i < count; i++) {
            myPlanets.get(i).getWeight(user.weight);
        }

        return;
    }

    public static double jobPromotion(Scanner scanner) {
        // Slide: 3
        // Page: 28
        String input, oldString, percentString, promotionValueString, updatedSalaryString;
        double salary, updatedSalary, percent, promotionValue;
        System.out.println("What\'s your salary: ");
        input = scanner.nextLine();
        salary = Double.parseDouble(input);
        updatedSalary = salary;

        if (salary < 2800) {
            percent = 1.2;
        } else if (salary < 7000) {
            percent = 1.15;
        } else if (salary < 15000) {
            percent = 1.1;
        } else {
            percent = 1.05;
        }

        updatedSalary *= percent;
        promotionValue = updatedSalary - salary;

        oldString = "Old salary: '" + salary + "'\n";
        percentString = "Promotion percent: '" + percent + "'\n";
        promotionValueString = "Promotion value: '" + promotionValue + "'\n";
        updatedSalaryString = "New Salary: '" + updatedSalary + "'\n";

        System.out.println(oldString + percentString + promotionValueString + updatedSalaryString);

        return updatedSalary;
    }

    public static void taxCalculator(Scanner scanner) {
        // Slide: 3
        // Page: 29
        double salary, ir, inss, totalTax, liquidSalary;
        System.out.println("What\'s your salary? ");
        String input = scanner.nextLine();
        salary = Double.parseDouble(input); // monthly salary
        // ir = 0.1; // revenue tax
        inss = 0.1; // retirement tax
        // double fgts = 0.11; // deposited only by the bank

        if (salary <= 900) {
            ir = 0;
        } else if (salary <= 1500) {
            ir = 0.05;
        } else if (salary <= 2500) {
            ir = 0.1;
        } else {
            ir = 0.2;
        }

        totalTax = (salary * ir) + (salary * inss);
        liquidSalary = salary - totalTax;

        System.out.println("Liquid Salary: " + liquidSalary);

    }
}
