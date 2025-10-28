import java.util.Scanner;

public class GuessTheNumberAttempts {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Welcome to Guess The Number!");
        System.out.print("Enter the smallest number: ");
        int min = sc.nextInt();

        System.out.print("Enter the largest number: ");
        int max = sc.nextInt();

        System.out.print("How many attempts do you want? ");
        int maxAttempts = sc.nextInt();

        int secretNumber = getRandomNumber(min, max);
        int guess;
        int attempts = 0;

        System.out.println("I've picked a number between " + min + " and " + max + ". Try to guess it!");

        while (attempts < maxAttempts) {
            System.out.print("Your guess: ");
            guess = sc.nextInt();
            attempts++;

            if (guess < secretNumber) {
                System.out.println("Too low!");
            } else if (guess > secretNumber) {
                System.out.println("Too high!");
            } else {
                System.out.println("🎉 Correct! The number was " + secretNumber + ".");
                System.out.println("You guessed it in " + attempts + " attempts.");
                sc.close();
                return;
            }

            System.out.println("Attempts left: " + (maxAttempts - attempts));
        }

        System.out.println("❌ Out of attempts! The number was " + secretNumber + ".");
        sc.close();
    }

    public static int getRandomNumber(int min, int max) {
        return (int)(Math.random() * (max - min + 1)) + min;
    }
}
