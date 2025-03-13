package university.oop;

public class User {
    public final String name;
    public final double weight;

    public User(String name, double weight) {
        this.name = name;
        this.weight = weight;
    }

    @Override
    public String toString() {
        return "Hello, '" + name + "' you weight: '" + weight + "'!";
    }

}
