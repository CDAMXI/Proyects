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

        // --- Title bar ---
        JPanel titleBar = new JPanel();
        JLabel titleText = new JLabel(title);
        titleText.setFont(new Font("Arial", Font.BOLD, 30));
        titleText.setForeground(Color.WHITE);
        titleBar.setBackground(Color.BLACK);
        titleBar.add(titleText);
        frame.add(titleBar, BorderLayout.NORTH);

        // --- Rules panel ---
        JTextArea rules = new JTextArea(
            """
            Tic Tac Toe Rules:
            1. The first player places X, the second player places O.
            2. On each turn, a symbol is placed in an empty square.
            3. The first player to get 3 in a row (horizontal, vertical, or diagonal) wins.
            4. If all squares are filled and no one wins, the game is a draw.
            Enjoy the game!
            
            """);
        rules.setEditable(false);
        rules.setFont(new Font("Arial", Font.PLAIN, 16));
        rules.setBackground(Color.BLACK);
        rules.setForeground(Color.WHITE);
        rules.setLineWrap(true);
        rules.setWrapStyleWord(true);

        JScrollPane scroll = new JScrollPane(rules);
        scroll.setPreferredSize(new Dimension(250, height));
        frame.add(scroll, BorderLayout.WEST);

        // --- Current player ---
        Random rand = new Random();
        final int[] currentPlayer = {rand.nextInt(2)};
        JPanel firstPlayer = new JPanel();
        JLabel firstPlayerLabel = new JLabel("Current Player: " + players[currentPlayer[0]]);
        firstPlayerLabel.setFont(new Font("Arial", Font.BOLD, 20));
        firstPlayer.add(firstPlayerLabel);
        frame.add(firstPlayer, BorderLayout.SOUTH);

        // --- Board ---
        JPanel board = new JPanel(new GridLayout(3, 3));
        board.setBackground(Color.BLACK);
        frame.add(board, BorderLayout.CENTER);

        // Estado del tablero
        String[][] boardState = new String[3][3];

        // Crear botones
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                JButton cell = new JButton();
                cell.setFont(new Font("Arial", Font.BOLD, 60));
                final int row = i;
                final int col = j;

                cell.addActionListener(e -> {
                    String symbol = players[currentPlayer[0]];
                    cell.setText(symbol);
                    cell.setEnabled(false);
                    boardState[row][col] = symbol;

                    if (checkWin(boardState, symbol)) {
                        JOptionPane.showMessageDialog(frame, symbol + " has won!");
                        // Block all buttons
                        for (Component c : board.getComponents()) {
                            c.setEnabled(false);
                        }
                        return;
                    }

                    // Change player
                    currentPlayer[0] = (currentPlayer[0] + 1) % 2;
                    firstPlayerLabel.setText("Current Player: " + players[currentPlayer[0]]);
                });

                board.add(cell);
            }
        }

        // --- Show final window---
        frame.setVisible(true);
    }

    public boolean checkWin(String[][] board, String symbol) {
        // Filas
        for (int i = 0; i < 3; i++) {
            if (symbol.equals(board[i][0]) &&
                symbol.equals(board[i][1]) &&
                symbol.equals(board[i][2])) {
                return true;
            }
        }
        // Columnas
        for (int i = 0; i < 3; i++) {
            if (symbol.equals(board[0][i]) &&
                symbol.equals(board[1][i]) &&
                symbol.equals(board[2][i])) {
                return true;
            }
        }
        // Diagonales
        if (symbol.equals(board[0][0]) &&
            symbol.equals(board[1][1]) &&
            symbol.equals(board[2][2])) {
            return true;
        }
        return symbol.equals(board[0][2]) &&
               symbol.equals(board[1][1]) &&
               symbol.equals(board[2][0]);
    }
}
