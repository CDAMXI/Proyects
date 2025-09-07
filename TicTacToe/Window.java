import java.awt.*;
import java.util.*;
import javax.swing.*;

public class Window {
    int width, height;
    String title;
    String[] players;
    public Window(int width, int height, String title, String[] players) {
        this.width = width;
        this.height = height;
        this.title = title;
        this.players = players;
    }

    public void display() {
    JFrame frame = new JFrame(title);
    frame.setSize(width, height);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setResizable(false);
    frame.setLayout(new BorderLayout());
    frame.setLocationRelativeTo(null);

    // Title bar
    JPanel titleBar = new JPanel();
    JLabel titleText = new JLabel(title);
    titleText.setFont(new Font("Arial", Font.BOLD, 30));
    titleText.setForeground(Color.WHITE);
    titleBar.setBackground(Color.BLACK);
    titleBar.add(titleText);
    frame.add(titleBar, BorderLayout.NORTH);

    // Current player
    Random rand = new Random();
    final int[] currentPlayer = {rand.nextInt(2)};
    JPanel firstPlayer = new JPanel();
    JLabel firstPlayerLabel = new JLabel("Current Player: " + players[currentPlayer[0]]);
    firstPlayerLabel.setFont(new Font("Arial", Font.BOLD, 20));
    firstPlayer.add(firstPlayerLabel);
    frame.add(firstPlayer, BorderLayout.SOUTH);

    // Game board
    JPanel board = new JPanel(new GridLayout(3, 3));
    board.setBackground(Color.BLACK);

    for (int i = 0; i < 9; i++) {
        JButton cell = new JButton();
        cell.setFont(new Font("Arial", Font.BOLD, 60));

        cell.addActionListener(e -> {
            cell.setText(players[currentPlayer[0]]);
            cell.setEnabled(false);
            currentPlayer[0] = (currentPlayer[0] + 1) % 2;
            firstPlayerLabel.setText("Current Player: " + players[currentPlayer[0]]);
        });

        board.add(cell);
    }
    frame.add(board, BorderLayout.CENTER);

    // Hacer visible al final
    frame.setVisible(true);
}


}
