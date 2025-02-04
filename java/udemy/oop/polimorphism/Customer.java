package oop.polimorphism;

public class Customer {
    private String name;
    private String email;
    private double creditLimit;

    public Customer() {
        this("User");
    }

    public Customer(String name) {
        this(name, "user@gmail.com");
    }

    public Customer(String name, String email) {
        this.name = name;
        this.email = email;
        this.creditLimit = 1000;
    }

    public Customer(String name, String email, double creditLimit) {
        this.name = name;
        this.email = email;
        this.creditLimit = creditLimit;
    }

    public String getName() {
        return name;
    }

    public String getEmail() {
        return email;
    }

    public double getCreditLimit() {
        return creditLimit;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setCreditLimit(double creditLimit) {
        this.creditLimit = creditLimit;
    }

    public void describeCustomer(int customerNumber) {
        String customerPresentation = String.format("Customer %x:\n", customerNumber);
        String customerName = String.format("\tName: '%s'.\n", this.name);
        String customerEmail = String.format("\tEmail: '%s'.\n", this.email);
        String customerCredit = String.format("\tCredit: '%.2f'.\n", this.creditLimit);
        String result = String.format(
                "%s %s %s %s",
                customerPresentation,
                customerName,
                customerEmail,
                customerCredit);
        System.out.println(result);
    }

}
