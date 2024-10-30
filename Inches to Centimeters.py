 import java.util.Scanner;

public class HeightConversion {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int heightInches = scanner.nextInt();
        double heightCm = heightInches * 2.54;
        System.out.printf("%.2f\n", heightCm);
    }
}
