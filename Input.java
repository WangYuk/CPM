import java.util.Scanner;

public class Input {
    private Scanner scanner;
    private AON aon;

    public Input(Scanner scanner,AON aon) {
        this.scanner = scanner;
        this.aon = aon;
    }

    public void input() {
        int actNum = 0;
        System.out.println("请输入活动数量：");
        actNum = Integer.parseInt(scanner.nextLine());
        System.out.println("请以“活动名称-DU”的格式输入各个活动，每个活动输入结束后请按回车");
        for (int i = 0;i < actNum; i++) {
            String act = scanner.nextLine();
            aon.addActivity(new Activity(act));
        }
        System.out.println("请输入起始活动：");
        String start = scanner.nextLine();
        aon.setStart(start);
        System.out.println("请输入终止活动：");
        String end = scanner.nextLine();
        aon.setEnd(end);
        System.out.println("请输入活动之间关系个数：");
        int relNum = Integer.parseInt(scanner.nextLine());
        System.out.println("请以“紧前活动-紧后活动-关系类型-时间”的格式输入活动间的关系，如果时间为负数，用“&”代替负号");
        for (int i = 0;i < relNum;i++) {
            String[] args = scanner.nextLine().split("-");
            Activity from = aon.getActivities().get(args[0]);
            Activity to = aon.getActivities().get(args[1]);
            int time = Integer.parseInt(args[3].replace('&','-'));
            aon.addRelation(new Relation(from,to,args[2],time));
        }
    }

}
