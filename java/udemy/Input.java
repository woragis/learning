import java.util.Scanner;

public class Input {

  static int currentYear = 2025;
  static boolean validBirthDate = false;

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("What's your name? ");
    String name = scanner.nextLine();
    int age = 0;

    do {
      try {
        System.out.println(
            "What year were you born? (enter a date between " + (currentYear - 125) + " and " + currentYear + ")");

        age = checkDates(currentYear, scanner.nextLine());
        validBirthDate = age < 0 || age > 125 ? false : true;

      } catch (NumberFormatException badInput) {
        System.err.println("\nError: You must use numbers only\n\n");
      }
    } while (!validBirthDate);

    System.out.println("Hello, " + name + "!");
    System.out.println("You are " + age + " years old!");
    scanner.close();
  }

  public static int checkDates(int currentYear, String birthDate) {
    int birthDateNumber = Integer.parseInt(birthDate);
    int minYear = currentYear - 125;
    if (birthDateNumber < minYear && birthDateNumber > currentYear) {
      return -1;
    }
    return (currentYear - birthDateNumber);
  }

  public static String getUserBirthYear(int currentYear) {
    String name = System.console().readLine("What's your name? ");
    int age = Integer.parseInt(System.console().readLine("How old are you? "));
    return name + " is " + age + "years old!\nAnd was born in " + (currentYear - age);
  }
}
