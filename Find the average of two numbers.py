 import java.util.Scanner;

public class AverageOfTwoNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double N = scanner.nextDouble();
        double M = scanner.nextDouble();
        double average = (N + M) / 2;
        System.out.printf("%.4f\n", average);
    }
}
