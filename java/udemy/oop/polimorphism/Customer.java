package oop.polimorphism;

public class Customer {
    String name;
    String email;
    double creditLimit;

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

    public String describeCustomer(int customerNumber) {
        String result = "Customer " + customerNumber + " information:\n\tName: " + this.name + "\n\tEmail: "
                + this.email
                + "\n\tCredit Limit: "
                + this.creditLimit + ".";
        System.out.println(result);
        return result;
    }

}
