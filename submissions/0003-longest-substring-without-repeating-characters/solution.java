class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.equals("")){
            return 0;
        }
        char[] str = s.toCharArray();
        int max, start, end;
        max = start = end = 0;
        for(int i = 1; i < str.length; i++){
            if(containsChar(str, start, end, str[i])){
                while(str[start] != str[i]){
                    start++;
                }
                start++;
            } else {
                
            }
            end = i;
            if(end - start > max) {
                max = end - start;
            }
            System.out.println("start: " + start + " end: " + end + " max: "  + max);
        }
        return max + 1;
    }
    

    public static boolean containsChar(char[] str, int min,int max, char c) {
        boolean ret = false;
        for(int i = min; i <= max; i++){
            if(str[i] == c){
                ret = true;
                break;
            }
        }
        return ret;
    }
}
