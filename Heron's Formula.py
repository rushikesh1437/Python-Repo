import java.util.Scanner;

public class TriangleArea {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();
        
        
        double s = (a + b + c) / 2.0;
        
        
        double area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
        
        
        System.out.printf("%.4f%n", area);
        
        scanner.close();
    }
}
