 import java.util.Scanner;

public class ProfitPercentage {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int CP = scanner.nextInt();
        int SP = scanner.nextInt();
        
        double profit = SP - CP;
        double profitPercentage = (profit / CP) * 100;

        System.out.printf("%.2f\n", profitPercentage);
    }
}
