 import java.util.Scanner;

public class CharacterCheck {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        char ch = scanner.next().charAt(0);
        
        if (ch >= 'A' && ch <= 'Z') {
            System.out.println("uppercase alphabet");
        } else if (ch >= 'a' && ch <= 'z') {
            System.out.println("lowercase alphabet");
        } else {
            System.out.println("not an alphabet");
        }
    }
}
