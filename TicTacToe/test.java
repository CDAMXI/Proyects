
public class test {
    public static void main(String[] args) {
        game();
    }

    public static void game() {
        Window window = new Window(900, 700, "Tic Tac Toe", new String[]{"X", "O"});
        window.display();
    }
}
