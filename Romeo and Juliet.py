 import java.util.Scanner;

public class MaximumChocolates {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int X = scanner.nextInt();
        int Y = scanner.nextInt();
        int Z = scanner.nextInt();
        
        int totalMoney = (X * 5) + (Y * 10);
        int maxChocolates = totalMoney / Z;
        
        System.out.println(maxChocolates);
    }
}
