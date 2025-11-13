package Others.Patterns;

import java.util.Scanner;

public class Patterns {

    public static void Pattern1(int n) {
        // Constant single column
        for (int i = 0; i < n; i++) {
            System.out.println("*");
        }
    }

    public static void Pattern2(int n) {
        // Constant right-aligned single column
        for (int i = 0; i < n; i++) {
            System.out.println(" ".repeat(n - 1) + "*");
        }
    }

    public static void Pattern3(int n) {
        // Left-aligned increasing triangle
        for (int i = 0; i < n; i++) {
            System.out.println("*".repeat(i + 1));
        }
    }

    public static void Pattern4(int n) {
        // Left-aligned decreasing triangle
        for (int i = 0; i < n; i++) {
            System.out.println("*".repeat(n - i));
        }
    }

    public static void Pattern5(int n) {
        // Right-aligned increasing triangle
        for (int i = 0; i < n; i++) {
            System.out.println(" ".repeat(n - i - 1) + "*".repeat(i + 1));
        }
    }

    public static void Pattern6(int n) {
        // Right-aligned decreasing triangle
        for (int i = 0; i < n; i++) {
            System.out.println(" ".repeat(i) + "*".repeat(n - i));
        }
    }

    public static void Pattern7(int n) {
        // Centered pyramid
        for (int i = 0; i < n; i++) {
            System.out.println(" ".repeat(n - i - 1) + "*".repeat(2 * i + 1));
        }
    }

    public static void Pattern8(int n) {
        // Inverted centered pyramid
        for (int i = 0; i < n; i++) {
            System.out.println(" ".repeat(i) + "*".repeat(2 * (n - i) - 1));
        }
    }

    public static void Pattern9(int n) {
        // Diamond
        for (int i = 0; i < n; i++) {
            System.out.println(" ".repeat(n - i - 1) + "*".repeat(2 * i + 1));
        }
        for (int i = n - 2; i >= 0; i--) {
            System.out.println(" ".repeat(n - i - 1) + "*".repeat(2 * i + 1));
        }
    }

    public static void main(String[] args) {

        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Enter the number of rows: ");
            int n = sc.nextInt();

            System.out.println("Pattern 1:");
            Pattern1(n);
            System.out.println();

            System.out.println("Pattern 2:");
            Pattern2(n);
            System.out.println();

            System.out.println("Pattern 3:");
            Pattern3(n);
            System.out.println();

            System.out.println("Pattern 4:");
            Pattern4(n);
            System.out.println();

            System.out.println("Pattern 5:");
            Pattern5(n);
            System.out.println();

            System.out.println("Pattern 6:");
            Pattern6(n);
            System.out.println();

            System.out.println("Pattern 7:");
            Pattern7(n);
            System.out.println();

            System.out.println("Pattern 8:");
            Pattern8(n);
            System.out.println();

            System.out.println("Pattern 9:");
            Pattern9(n);
        }
    }
}

