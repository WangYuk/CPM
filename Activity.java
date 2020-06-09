import java.util.ArrayList;
import java.util.HashMap;

public class Activity {
    private int earlyStart;
    private int totalFloat;
    private int earlyFinish;
    private int duration;
    private int lateFinish;
    private int freeFloat;
    private int lateStart;
    private boolean isStart = false;
    private boolean isEnd = false;
    private String name;
    private ArrayList<Relation> preRelations = new ArrayList<>();
    private ArrayList<Relation> sucRelations = new ArrayList<>();

    public Activity (String name,int duration) {
        this.name = name;
        this.duration = duration;
    }

    public Activity (String act) {
        String[] args = act.split("-");
        name = args[0];
        duration = Integer.parseInt(args[1]);
    }

    public void addPre(Relation relation) {
        preRelations.add(relation);
    }

    public void addSuc(Relation relation) {
        sucRelations.add(relation);
    }

    public void calEarly() {
        if (isStart) {
            earlyStart = 0;
            earlyFinish = earlyStart + duration;
            return;
        }
        int max = Integer.MIN_VALUE;
        for (Relation relation: preRelations) {
            if (relation.getTime() + relation.getFrom().getEarlyFinish() > max) {
                max = relation.getTime() + relation.getFrom().getEarlyFinish();
            }
        }
        earlyStart = max;
        earlyFinish = earlyStart + duration;
    }

    public void calLate() {
        if (isEnd) {
            lateFinish = earlyFinish;
            lateStart = earlyStart;
            return;
        }
        int min = Integer.MAX_VALUE;
        for (Relation relation:sucRelations) {
            if (relation.getTo().lateStart - relation.getTime() < min) {
                min = relation.getTo().lateStart - relation.getTime();
            }
        }
        lateFinish = min;
        lateStart = lateFinish - duration;
    }

    public void calFloat() {
        if (isEnd || isStart) {
            totalFloat = 0;
            freeFloat = 0;
            return;
        }
        totalFloat = lateFinish - earlyFinish;
        int min = Integer.MAX_VALUE;
        for (Relation relation: sucRelations
             ) {
            if (min > relation.getTo().earlyStart - relation.getTime() - earlyFinish) {
                min = relation.getTo().earlyStart - relation.getTime() - earlyFinish;
            }
        }
        freeFloat = min;
    }

    public int getEarlyFinish() {
        return earlyFinish;
    }

    public String getName() {
        return name;
    }

    public int getTotalFloat() {
        return totalFloat;
    }

    public void calKeyRoad(ArrayList<Activity> road) {
        if (isEnd) {
            boolean isfirst = true;
            for (Activity act:road
                 ) {
                if (isfirst) {
                    System.out.print(act.getName());
                    isfirst = false;
                }
                else {
                    System.out.print("->" + act.getName());
                }
            }
            System.out.println("");
            return;
        }
        for (Relation relation:sucRelations
             ) {
            if (relation.getTo().getTotalFloat() == 0) {
                road.add(relation.getTo());
                relation.getTo().calKeyRoad(road);
                road.remove(relation.getTo());
            }
        }
    }

    public int getDuration() {
        return duration;
    }

    public void setStart(boolean start) {
        isStart = start;
    }

    public void setEnd(boolean end) {
        isEnd = end;
    }

    public ArrayList<Relation> getPreRelations() {
        return preRelations;
    }

    public ArrayList<Relation> getSucRelations() {
        return sucRelations;
    }

    public void print() {
        System.out.println("---------------------------------");
        System.out.println("ES: " + earlyStart + "  TF: "+ totalFloat + "  EF:" + earlyFinish);
        System.out.println("name:  " + name + "   DU: " + duration);
        System.out.println("LS: " + lateStart + "  FF:" + freeFloat + "  LF:" + lateFinish);
        System.out.println("---------------------------------");
    }
}
