import java.util.*;

class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        Set<String> banset = new HashSet<>();
        for (String word : banned) {
            banset.add(word);
        }

        Map<String, Integer> count = new HashMap<>();
        String[] words = paragraph.replaceAll("\\W+", " ").toLowerCase().split("\\s+");
        for (String word : words) {
            if (!banset.contains(word)) {
                count.put(word, count.getOrDefault(word, 0) + 1);
            }
        }

        String result = "";
        int max = 0;
        for (String key : count.keySet()) {
            if (count.get(key) > max) {
                max = count.get(key);
                result = key;
            }
        }

        return result;
    }
}
