package oop.school;

public class Main {
    public static void main(String[] args) {

        for (int i = 0; i < 5; i++) {
            LPAStudent s = new LPAStudent("09984" + i,
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
        LPAStudent jezreel = new LPAStudent("1", "Jezreel", "12/03/2004",
                "ComputerScience - UFBP, Java Masterclass - Udemy, CS50 - Edx");
        System.out.println(jezreel);
    }
}
