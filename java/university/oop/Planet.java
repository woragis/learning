package university.oop;

public class Planet {
    private final String planetName;
    private final double gravity;

    public Planet(String planetName, double gravity) {
        this.planetName = planetName;
        this.gravity = gravity;
    }

    public double getWeight(double weight) {
        double result = this.gravity * weight;
        System.out.println("Weight on '" + planetName + "' = '" + result + "'");
        return result;
    }

    @Override
    public String toString() {
        return "Planet [planetName=" + planetName + ", gravity=" + gravity + "]";
    }

}
