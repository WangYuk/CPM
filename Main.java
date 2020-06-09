import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        AON aon = new AON();
        Input input = new Input(scanner,aon);
        input.input();
        aon.calEarly();
        aon.calLate();
        aon.calFloat();
        aon.print();
        System.out.println("key roads:");
        aon.findKeyRoad();
    }
}
