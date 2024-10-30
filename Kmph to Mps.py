 import java.util.Scanner;

public class SpeedConversion {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int speedKmph = scanner.nextInt();
        double speedMps = speedKmph * 1000.0 / 3600.0;
        System.out.printf("%.2f\n", speedMps);
    }
}
