class Solution {
    public String[] reorderLogFiles(String[] logs) {
        if(logs == null || logs.length == 0) 
            return logs;

        int len = logs.length;
        List<String> letterList = new ArrayList<>();
        List<String> digitList = new ArrayList<>();

        for(int i = 0; i < len; i++) {
            if(isDigitLog(logs[i])) {
                digitList.add(logs[i]);
            } else {
                letterList.add(logs[i]);
            }
        }

        Collections.sort(letterList, (o1, o2) -> {
            String[] split1 = o1.split(" ", 2);
            String[] split2 = o2.split(" ", 2);
            int cmp = split1[1].compareTo(split2[1]);
            if(cmp != 0) 
                return cmp;
            return split1[0].compareTo(split2[0]);
        });

        int i = 0;
        for(String log : letterList) {
            logs[i++] = log;
        }

        for(String log : digitList) {
            logs[i++] = log;
        }

        return logs;
    }

    private boolean isDigitLog(String log) {
        return Character.isDigit(log.split(" ", 2)[1].charAt(0));
    }
}