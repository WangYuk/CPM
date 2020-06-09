public class Relation {
    private Activity from;
    private Activity to;
    private int time;
    private RelationType relationType;

    public Relation(Activity from,Activity to,String type,int time) {
        this.from = from;
        this.to = to;
        this.relationType = RelationType.valueOf(type);
        this.time = time;
        toFS();
    }

    public void toFS() {
        if (relationType == RelationType.FS) {
            return;
        }
        if (relationType == RelationType.SF) {
            time = time - from.getDuration() - to.getDuration();
            relationType = RelationType.FS;
            return;
        }
        if (relationType == RelationType.SS) {
            time = time - from.getDuration();
            relationType = RelationType.FS;
            return;
        }
        time = time - to.getDuration();
        relationType = RelationType.FS;
    }

    public Activity getFrom() {
        return from;
    }

    public Activity getTo() {
        return to;
    }

    public int getTime() {
        return time;
    }
}
