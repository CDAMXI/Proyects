import java.awt.*;
import java.util.*;
import javax.swing.*;

public class test {
    public static void main(String[] args) {
        game();
    }

    public static void game() {
        Window window = new Window(900, 700, "Tic Tac Toe");
        window.display();
        String[][] board = new String[3][3];
        String[] players = {"X", "O"};
        Random rand = new Random();
        int currentPlayer = rand.nextInt(2); // Randomly select starting player

        // First player
        JPanel firstPlayer = new JPanel();
        JLabel firstPlayerLabel = new JLabel();
        firstPlayerLabel.setText("Current Player: " + players[currentPlayer]);
        firstPlayer.add(firstPlayerLabel);

        firstPlayerLabel.setFont(new Font("Arial", Font.BOLD, 20)); // Font size for player turn display
        firstPlayer.add(firstPlayerLabel);
        System.out.println();
    }
}
