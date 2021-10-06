func letterCombinations(digits string) []string {
    if digits == "" {
        return []string{}
    }
    ret := strings.Split(getLetters(int(digits[0]) - '0'), "")  
    for _, v := range(digits[1:]) {
        curr := getLetters(int(v) - '0')
        new_ret := []string{}
        for _, i := range(curr){
            for _, j := range(ret) {
                new_ret = append(new_ret, string(j) + string(i))
            }
        }
        ret = new_ret
    }
    return ret
}

func getLetters(key int) string {
    return map[int]string{
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz",
    }[key]
}
