package university.oop.list;

import java.util.ArrayList;
import java.util.Scanner;

public class MyListExercises {
    public static void main() {
        ArrayList<Integer> myNumbers = new ArrayList<Integer>();
        myNumbers.add(3);
        myNumbers.add(8);
        Sum(myNumbers);

        ArrayList<Double> myNotes = new ArrayList<Double>();
        myNotes.add(8.0);
        myNotes.add(6.0);
        myNotes.add(9.0);
        myNotes.add(8.0);
        schoolMedian(myNotes);

        metersToCentimeters(4);

        circleArea(4.0);

        Scanner scanner = new Scanner(System.in);
        monthlySalary(scanner);
        scanner.close();

    }

    public static int Sum(ArrayList<Integer> nums) {
        int sum = 0;
        int numsSize = nums.size();

        System.out.print("The sum of: ");
        for (int i = 0; i < numsSize; i++) {
            sum += nums.get(i);
            System.out.print("'" + nums.get(i) + "', ");
        }
        System.out.println("is equal to: '" + sum + "'");
        return sum;
    }

    public static double schoolMedian(ArrayList<Double> notes) {
        double sum = 0;
        int notesSize = notes.size();

        System.out.print("The median of: ");
        for (int i = 0; i < notesSize; i++) {
            sum += notes.get(i);
            System.out.print("'" + notes.get(i) + "', ");
        }
        System.out.println("is equal to: '" + sum + "'");
        System.out.println("And the median is: '" + (sum / notesSize) + "'");

        return sum / notesSize;
    }

    public static int metersToCentimeters(int meter) {
        System.out.println("'" + meter + "' meters is '" + (meter * 100) + "' in centimeters");
        return meter * 100;
    }

    public static double circleArea(double radius) {
        double result = (2 * radius) * (3.14 * 3.14);
        System.out.println("The area of a circle with '" + radius + "' of radius is: '" + result + "'");
        return result;
    }

    public static int squareArea(int sideSize) {
        int area = sideSize * sideSize;
        int doubledArea = area * 2;
        System.out.println("The area of a square with '" + sideSize + "' of size is: '" + area
                + "' and the doubled area is: '" + doubledArea + "'");
        return doubledArea;
    }

    public static double monthlySalary(Scanner scanner) {
        String input;
        double salary, result;
        int hours;
        System.out.print("How much do you earn per hour? ");
        input = scanner.nextLine();
        salary = Double.parseDouble(input);

        System.out.print("How many hours do you work per month? ");
        input = scanner.nextLine();
        hours = Integer.parseInt(input);

        result = salary * hours;
        System.out.println("Based on what you gave me.. you earn: '" + result + "' per month");

        return result;
    }

    public static double fahrenheitToCelsius(double fahrenheit) {
        double celsius = ((fahrenheit - 32) / 9) * 5;
        System.out.println("'" + fahrenheit + "' Fahrenheit in Celsius is: '" + celsius + "'");
        return celsius;
    }

    public static double celsiusToFahrenheit(double celsius) {
        double fahrenheit = ((celsius / 5) * 9) + 32;
        System.out.println("'" + celsius + "' Celsius in Fahrenheit is: '" + fahrenheit + "'");
        return fahrenheit;
    }

    public static void calculus(int num1, int num2, double num3) {
        double first = num1 * num1 * (num2 / 2);
        double second = (num1 * 3) + num3;
        double third = Math.pow(num3, 3);
        System.out.println("First operation result: '" + first + "'");
        System.out.println("Second operation result: '" + second + "'");
        System.out.println("Third operation result: '" + third + "'");
        return;
    }

    public static double idealWeight(double height) {
        double weight = (72.7 * height) - 58;
        System.out.println("Based on your height '" + height + "' your ideal weight is: '" + weight + "'");
        return weight;
    }

    public static double idealWeight(double height, String gender) {
        gender = gender.toLowerCase();
        if (gender == "male") {
            return idealWeight(height);
        } else if (gender == "female") {
            double weight = (height * 62.1) - 44.7;
            System.out.println("Based on your height '" + height + "' your ideal weight is: '" + weight + "'");
            return weight;
        } else {
            return 0.0;
        }
    }
}
