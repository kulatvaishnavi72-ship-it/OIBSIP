import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

/**
 * Number Guessing Game — Oasis Infobyte SIP, Java Track, Task 2
 *
 * The computer picks a random number; the user guesses with
 * higher/lower hints, a limited number of attempts, difficulty
 * levels, and a running score summary across rounds.
 */
public class NumberGuessingGame {

    private static final Scanner scanner = new Scanner(System.in);
    private static final Random random = new Random();
    private static final List<String> roundSummaries = new ArrayList<>();

    public static void main(String[] args) {
        System.out.println("========================================");
        System.out.println("      NUMBER GUESSING GAME");
        System.out.println("========================================");

        int round = 1;
        boolean playAgain = true;

        while (playAgain) {
            System.out.println("\n--- Round " + round + " ---");
            playRound(round);
            round++;

            System.out.print("\nPlay again? (y/n): ");
            String answer = scanner.nextLine().trim().toLowerCase();
            playAgain = answer.equals("y");
        }

        System.out.println("\n========================================");
        System.out.println("            FINAL SUMMARY");
        System.out.println("========================================");
        for (String summary : roundSummaries) {
            System.out.println(summary);
        }
        System.out.println("\nThanks for playing!");
    }

    private static void playRound(int round) {
        Difficulty difficulty = chooseDifficulty();
        int secret = random.nextInt(difficulty.max) + 1;
        int attempts = 0;
        boolean won = false;

        System.out.println("I'm thinking of a number between 1 and " + difficulty.max
                + ". You have " + difficulty.maxAttempts + " attempts.");

        while (attempts < difficulty.maxAttempts) {
            System.out.print("Attempt " + (attempts + 1) + "/" + difficulty.maxAttempts + " — your guess: ");
            String input = scanner.nextLine().trim();

            int guess;
            try {
                guess = Integer.parseInt(input);
            } catch (NumberFormatException e) {
                System.out.println("  ⚠ Please enter a whole number.");
                continue;
            }

            attempts++;

            if (guess == secret) {
                System.out.println("Correct! 🎉");
                won = true;
                break;
            } else if (guess < secret) {
                System.out.println("Too Low!");
            } else {
                System.out.println("Too High!");
            }
        }

        String summary;
        if (won) {
            summary = "Round " + round + " — guessed in " + attempts + " attempts (Difficulty: " + difficulty.name + ")";
            System.out.println(summary);
        } else {
            System.out.println("You Lost! The number was: " + secret);
            summary = "Round " + round + " — lost after " + attempts + " attempts (Difficulty: " + difficulty.name + ")";
        }
        roundSummaries.add(summary);
    }

    private static Difficulty chooseDifficulty() {
        while (true) {
            System.out.print("Choose difficulty — Easy (1-50, 10 attempts) / Medium (1-100, 7) / Hard (1-200, 5): ");
            String choice = scanner.nextLine().trim().toLowerCase();
            switch (choice) {
                case "easy": return new Difficulty("Easy", 50, 10);
                case "medium": return new Difficulty("Medium", 100, 7);
                case "hard": return new Difficulty("Hard", 200, 5);
                default:
                    System.out.println("  ⚠ Please type: easy, medium, or hard.");
            }
        }
    }

    private static class Difficulty {
        final String name;
        final int max;
        final int maxAttempts;

        Difficulty(String name, int max, int maxAttempts) {
            this.name = name;
            this.max = max;
            this.maxAttempts = maxAttempts;
        }
    }
}
