import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        int decimalValue = Integer.parseInt(s, 8);
        System.out.println(decimalValue);
    }
}
