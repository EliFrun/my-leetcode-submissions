class Solution {
    public int romanToInt(String s) {
        HashMap<String, Integer> key = new HashMap<String, Integer>();
        key.put("M", 1000);
        key.put("D", 500);
        key.put("C", 100);
        key.put("L", 50);
        key.put("X", 10);
        key.put("V", 5);
        key.put("I", 1);
        
        int ret = 0;
        for(int i = 0; i < s.length(); i++){
            int f = key.get(Character.toString(s.charAt(i)));
            if(f <  key.get(Character.toString(s.charAt( i < s.length() - 1 ? i + 1 : i)))){
                ret -= f;
            } else {
                ret += f;
            }
        }
        return ret;
    }
}
