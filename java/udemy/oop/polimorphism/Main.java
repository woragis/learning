package oop.polimorphism;

public class Main {

    public static void main(String[] args) {
        Car car1 = new Car("Porsche", "911", "White", 2, false);
        Car car2 = new Car("Volkswagen", "Polo");
        Car car3 = new Car("BMW", "M3", "Blue");

        System.out.println("\nCar 1:");
        car1.describeCar();

        System.out.println("\nCar 2:");
        car2.describeCar();

        System.out.println("\nCar 3:");
        car3.describeCar();
    }
}
