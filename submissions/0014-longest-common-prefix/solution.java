class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length == 0){
            return "";
        }
        String shortestString = "";
        int max = 13123131;
        for(String s: strs){
            if(s.length() < max){
                max = s.length();
            }
        }
        
        String ret = "";
        for(int i = 0; i<max; i++){
            char currentChar = strs[0].charAt(i);
            for(String s: strs){
                if(s.charAt(i) != currentChar){
                    return ret;
                }
            }
            ret += currentChar;
        }
        
        return ret;
    }
}
