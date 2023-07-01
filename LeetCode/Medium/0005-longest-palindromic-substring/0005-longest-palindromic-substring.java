class Solution {
    public String longestPalindrome(String s) {
    	if (s.length() < 2 && s.equals(new StringBuffer(s).reverse().toString())) {
    		return s;
    	}
    	
    	String result = "";
    	for (int i = 0; i < s.length(); i++) {
    		String even = this.expand(s, i, i + 1, s.length());
    		String odd = this.expand(s, i, i + 2, s.length());
    		
    		if (result.length() < even.length()) {
    			result = even;
    		}
    		if (result.length() < odd.length()) {
    			result = odd;
    		}
    	}
    	
        return result;
    }
    
    public String expand(String s, int left, int right, int len) {
    	try {
            while (left >= 0 && right < len && s.charAt(left) == s.charAt(right)) {
                left--;
                right++;
            }
            return s.substring(left + 1, right);
		} catch (IndexOutOfBoundsException e) {
			return "";
        }
    }
}