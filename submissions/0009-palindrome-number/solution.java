class Solution {
    public boolean isPalindrome(int x) {
        String s = Integer.toString(x);
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
