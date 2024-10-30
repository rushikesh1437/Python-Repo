 import java.util.Scanner;

public class RainfallCategory {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int x = scanner.nextInt();
        
        if (x < 3) {
            System.out.println("LIGHT");
        } else if (x >= 3 && x < 7) {
            System.out.println("MODERATE");
        } else {
            System.out.println("HEAVY");
        }
    }
}
