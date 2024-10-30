 import java.util.Scanner;

public class FahrenheitToCelsius {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int F = scanner.nextInt();
        double C = (F - 32) * 5.0 / 9.0;
        System.out.printf("%.2f%n", C);
    }
}
