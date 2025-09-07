import java.awt.*;
import javax.swing.*;

public class Window {
    int width, height;
    String title;
    public Window(int width, int height, String title) {
        this.width = width;
        this.height = height;
        this.title = title;
    }

    public void display() {
        // Create the window
        JFrame frame = new JFrame(title);
        frame.setSize(width, height);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setResizable(false);

        // Create title bar
        JPanel titleBar = new JPanel();
        JLabel titleText = new JLabel(title);
        titleText.setFont(new Font("Arial", Font.BOLD, 30));
        titleBar.add(titleText);
        frame.add(titleBar, BorderLayout.NORTH);

        // Set colors
        titleText.setForeground(Color.WHITE);
        titleBar.setBackground(Color.BLACK);
        frame.getContentPane().setBackground(Color.BLACK);
    }
}
