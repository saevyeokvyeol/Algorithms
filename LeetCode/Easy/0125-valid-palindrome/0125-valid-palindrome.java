class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        s = s.replaceAll("[^a-z0-9]", "");

        String reverseS = new StringBuilder(s).reverse().toString();
        return s.equals(reverseS);
    }
}