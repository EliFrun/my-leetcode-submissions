class Solution {
    public String intToRoman(int num) {
        if(num == 0){
            return "";
        }
        String s = "";
        HashMap<Integer, String> key = new HashMap<Integer, String>();
        key.put(1000, "M");
        key.put(500, "D");
        key.put(100, "C");
        key.put(50, "L");
        key.put(10, "X");
        key.put(5, "V");
        key.put(1, "I");
        
        int size = Integer.toString(num).length();
        int letter = (int)Math.pow(10, size - 1);
        int q = num / letter;
        int r = num % letter;

        if (q == 4) {
            s += key.get(letter);
            s += key.get(letter * 5);
        } else if (q == 9) {
            s += key.get(letter);
            s += key.get(letter*10);
        } else if (q >= 5) {
            s += (key.get(5*letter));
            for(int i = 0; i < q - 5; i++){
                s+= key.get(letter);
            }
        } else {
            for(int i = 0; i < q; i++){
                s+= key.get(letter);
            }
        }
        
        
        
        return s + intToRoman(r);
    }
}
