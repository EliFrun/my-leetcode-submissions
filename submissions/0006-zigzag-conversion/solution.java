class Solution {
    public String convert(String s, int numRows) {
        if(numRows == 1 || s.equals("")){
            return s;
        }
        String ret = "";
        int zigzag = (numRows) * (s.length()/(numRows + numRows/2) + 1);
        char[][] board = new char[numRows][zigzag];
        int currentCharIndex = 0;
        int column = 0;
        try{
           while(currentCharIndex < s.length()){
                for(int i = 0; i < numRows; i++){
                    board[i][column] = s.charAt(currentCharIndex++);
                }
                column++;
                for(int i = numRows - 2; i > 0; i--){
                    board[i][column++] = s.charAt(currentCharIndex++);
                }
            }  
        } catch (Exception e){
            
        }
        for(char[] row: board){
            for(char c: row){
                if(c != '\0'){
                    ret = ret + c;
                }
            }
        }
        return ret;
    }
}
