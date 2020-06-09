public enum  RelationType {
    FS,
    SS,
    SF,
    FF;

    public RelationType string2type(String name) {
        if (name.equals("FS")) {
            return FS;
        }
        if (name.equals("SS")) {
            return SS;
        }
        if (name.equals("SF")) {
            return SF;
        }
        return FF;
    }

}
