import java.util.Scanner;

public class InteriorDesignCost {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int X1 = scanner.nextInt();
        int Y1 = scanner.nextInt();
        int X2 = scanner.nextInt();
        int Y2 = scanner.nextInt();
        
        int costStyle1 = X1 + Y1;
        int costStyle2 = X2 + Y2;
        
        System.out.println(Math.min(costStyle1, costStyle2));
    }
}
