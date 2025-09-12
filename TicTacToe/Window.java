import java.awt.*;
import java.awt.event.*;
import java.util.*;
import javax.swing.*;
import javax.swing.border.LineBorder;

public class Window {
    int width, height;
    String title;
    String[] players;
    private boolean closed = false; // Flag para saber si la ventana se cerró

    public Window(int width, int height, String title, String[] players) {
        this.width = width;
        this.height = height;
        this.title = title;
        this.players = players;
    }

    public void display() {
        JFrame frame = new JFrame(title);
        frame.setSize(width, height);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.setResizable(false);
        frame.setLayout(new BorderLayout());
        frame.setLocationRelativeTo(null);

        // Listener para detectar cierre
        frame.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosed(WindowEvent e) {
                closed = true;
            }
        });

        // --- Title bar ---
        JPanel titleBar = new JPanel();
        JLabel titleText = new JLabel(title);
        titleText.setFont(new Font("Arial", Font.BOLD, 30));
        titleText.setForeground(Color.decode("#FFD93D")); // Amarillo
        titleBar.setBackground(Color.decode("#4F200D")); // Marrón oscuro
        titleBar.add(titleText);
        frame.add(titleBar, BorderLayout.NORTH);

        // --- Current player ---
        Random rand = new Random();
        final int[] currentPlayer = {rand.nextInt(2)};
        JPanel firstPlayer = new JPanel();
        firstPlayer.setBackground(Color.decode("#4F200D")); // Marrón oscuro
        JLabel firstPlayerLabel = new JLabel("Current Player: " + players[currentPlayer[0]]);
        firstPlayerLabel.setFont(new Font("Arial", Font.BOLD, 20));
        firstPlayerLabel.setForeground(Color.decode("#FFD93D")); // Amarillo
        firstPlayer.add(firstPlayerLabel);
        frame.add(firstPlayer, BorderLayout.SOUTH);

        // --- Board ---
        Color boardColor = Color.decode("#4F200D");
        JPanel board = new JPanel(new GridLayout(3, 3));
        board.setBackground(boardColor);
        frame.add(board, BorderLayout.CENTER);

        // Estado del tablero
        String[][] boardState = new String[3][3];

        // Crear botones con borde y color que se mantiene
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                JButton cell = new JButton();
                cell.setFont(new Font("Arial", Font.BOLD, 60));

                // Color inicial según jugador (X naranja, O amarillo)
                cell.setForeground(Color.decode("#FF9A00")); // Naranja para texto inicial
                cell.setBackground(Color.decode("#FFD93D")); // Amarillo inicial
                cell.setOpaque(true);
                cell.setBorder(new LineBorder(boardColor, 3)); // Borde del color del tablero

                final int row = i;
                final int col = j;

                cell.addActionListener(e -> {
                    String symbol = players[currentPlayer[0]];
                    cell.setText(symbol);

                    // Cambiar color del texto según jugador
                    if (symbol.equals("X")) {
                        cell.setForeground(Color.decode("#FF9A00")); // Naranja
                    } else {
                        cell.setForeground(Color.decode("#4F200D")); // Marrón oscuro
                    }

                    cell.setEnabled(false);
                    boardState[row][col] = symbol;

                    // Comprobar victoria
                    if (checkWin(boardState, symbol)) {
                        JOptionPane.showMessageDialog(frame, symbol + " has won!");
                        for (Component c : board.getComponents()) {
                            c.setEnabled(false);
                        }
                        return;
                    }

                    // Cambiar de jugador
                    currentPlayer[0] = (currentPlayer[0] + 1) % 2;
                    firstPlayerLabel.setText("Current Player: " + players[currentPlayer[0]]);
                });

                board.add(cell);
            }
        }

        // --- Mostrar ventana ---
        frame.setVisible(true);
    }

    // Método para saber si la ventana se cerró
    public boolean isClosed() {
        return closed;
    }

    public boolean checkWin(String[][] board, String symbol) {
        for (int i = 0; i < 3; i++) {
            if (symbol.equals(board[i][0]) &&
                symbol.equals(board[i][1]) &&
                symbol.equals(board[i][2])) {
                return true;
            }
        }
        for (int i = 0; i < 3; i++) {
            if (symbol.equals(board[0][i]) &&
                symbol.equals(board[1][i]) &&
                symbol.equals(board[2][i])) {
                return true;
            }
        }
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
