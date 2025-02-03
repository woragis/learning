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

        Customer customer1 = new Customer();
        Customer customer2 = new Customer("Jezreel");
        Customer customer3 = new Customer("Israel", "israel@gmail.com");
        Customer customer4 = new Customer("Jefferson", "jefferson@gmail.com", 2000);

        customer1.describeCustomer(1);
        customer2.describeCustomer(2);
        customer3.describeCustomer(3);
        customer4.describeCustomer(4);
    }
}
