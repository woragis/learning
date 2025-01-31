public class Variables {
  public static void main(String[] args) {
    int myFirstNumber = 35;
    int mySecondNumber = 12;
    int myThirdNumber = 6;

    int myTotal = myFirstNumber + mySecondNumber + myThirdNumber; // 53

    myThirdNumber = myFirstNumber * 2; // 70
    myTotal = myFirstNumber + mySecondNumber + myThirdNumber; // 117

    int myLastNumber = 1000 - myTotal; // 883

    System.out.println(myLastNumber);
  }
}
