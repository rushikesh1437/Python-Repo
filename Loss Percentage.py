import java.util.Scanner;

public class LossPercentage {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
    
        double CP = scanner.nextDouble();
        double SP = scanner.nextDouble();
        
        
        double loss = CP - SP;
        
        
        double lossPercentage = (loss / CP) * 100;
        
        
        System.out.printf("%.2f%n", lossPercentage);
        
        scanner.close();
    }
}
