func maximumWealth(accounts [][]int) int {
    max := 0
    for _, v := range(accounts) {
        sum := 0
        for _, val := range(v) {
            sum += val
        }
        if sum > max {
            max = sum
        }
    }
    return max
}
