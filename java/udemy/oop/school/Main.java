package oop.school;

public class Main {
    public static void main(String[] args) {

        for (int i = 0; i < 5; i++) {
            Student s = new Student("09984" + i,
                    switch (i) {
                        case 0 -> "Mary";
                        case 1 -> "Carol";
                        case 2 -> "Tim";
                        case 3 -> "Harry";
                        case 4 -> "Lisa";
                        default -> "Anonymous";
                    },
                    "12/03/2004",
                    "Computer Science - UFPB");

            System.out.println(s);
        }
    }
}
