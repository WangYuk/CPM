import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

public class AON {
    private HashMap<String,Activity> activities = new HashMap<>();
    private HashMap<Activity,ArrayList<Relation>> relations = new HashMap<>();
    private Activity start;
    private Activity end;

    public void addActivity(Activity act) {
        activities.put(act.getName(),act);
    }

    public void addRelation(Relation relation) {
        if (!relations.containsKey(relation.getFrom())) {
            relations.put(relation.getFrom(),new ArrayList<>());
        }
        relations.get(relation.getFrom()).add(relation);
        relation.getFrom().addSuc(relation);
        relation.getTo().addPre(relation);
    }

    public void setStart(String name) {
        start = activities.get(name);
        start.setStart(true);
    }

    public void setEnd(String name) {
        end = activities.get(name);
        end.setEnd(true);
    }

    public void calEarly() {
        Queue<Activity> nextAct = new LinkedList<>();
        ArrayList<Activity> visited = new ArrayList<>();
        nextAct.add(start);
        visited.add(start);
        while (nextAct.size() != 0) {
            Activity toCal = nextAct.poll();
            toCal.calEarly();
            for (Relation relation:toCal.getSucRelations()
                 ) {
                if (!visited.contains(relation.getTo())) {
                    nextAct.add(relation.getTo());
                    visited.add(relation.getTo());
                }
            }
        }
    }

    public void calLate() {
        Queue<Activity> nextAct = new LinkedList<>();
        ArrayList<Activity> visited = new ArrayList<>();
        nextAct.add(end);
        visited.add(end);
        while (nextAct.size() != 0) {
            Activity toCal = nextAct.poll();
            toCal.calLate();
            for (Relation relation:toCal.getPreRelations()
            ) {
                if (!visited.contains(relation.getFrom())) {
                    nextAct.add(relation.getFrom());
                    visited.add(relation.getFrom());
                }
            }
        }
    }

    public void calFloat() {
        for (String name:activities.keySet()
             ) {
            activities.get(name).calFloat();
        }
    }

    public void findKeyRoad() {
        ArrayList<Activity> road = new ArrayList<>();
        road.add(start);
        start.calKeyRoad(road);
    }

    public void print() {
        Queue<Activity> nextAct = new LinkedList<>();
        ArrayList<Activity> visited = new ArrayList<>();
        nextAct.add(start);
        visited.add(start);
        while (nextAct.size() != 0) {
            Activity toCal = nextAct.poll();
            toCal.print();
            for (Relation relation:toCal.getSucRelations()
            ) {
                if (!visited.contains(relation.getTo())) {
                    nextAct.add(relation.getTo());
                    visited.add(relation.getTo());
                }
            }
        }
    }

    public HashMap<String, Activity> getActivities() {
        return activities;
    }
}
