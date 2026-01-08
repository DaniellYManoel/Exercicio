public class LogLevels {
    
    public static String message(String logLine) {
        return logLine
            .substring(logLine.indexOf(": ") + 2)
        .trim();
        }
    

    public static String logLevel(String logLine) {
        int inicio = logLine.indexOf("[") + 1;
        int fim = logLine.indexOf("]");
        return logLine.substring(inicio, fim).toLowerCase();
    }

    public static String reformat(String logLine) {
        return message(logLine) + " (" +logLevel(logLine) + ")";
    }

    public static void main(String[] args) {
        System.out.println(LogLevels.message("[ERROR]: Invalid operation"));
        System.out.println(LogLevels.message("[WARNING]: Something is wrong"));
    }
}
