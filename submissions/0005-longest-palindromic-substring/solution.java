class Solution {
    public String longestPalindrome(String s) {
        int currentMax = 1;
        String maxString = s.substring(0,1);
        for(int i = 0; i < s.length() - 1; i++){
            if(currentMax > s.length() - i){
                break;
            }
            char cur = s.charAt(i);
            for(int j = s.length() - 1; j >= i + 1; j--){
                if(s.charAt(i) == s.charAt(j)){
                    String foo = s.substring(i, j + 1);
                    if (isPalindrome(foo) && foo.length() > currentMax){
                        currentMax = foo.length();
                        maxString = foo;
                    }
                }
            }
        }
        return maxString;
    }
    
    private static boolean isPalindrome(String s){
        boolean ret = true;
        for(int i = 0; i < s.length()/2; i++){
            if(s.charAt(i) != s.charAt(s.length() - i - 1)){
                ret = false;
                break;
            }
        }
        return ret;
    }
}
