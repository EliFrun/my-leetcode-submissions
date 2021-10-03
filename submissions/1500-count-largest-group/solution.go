func countLargestGroup(n int) int {
    m := make(map[int]int)
    for i := 1; i <= n; i++ {
        sum := 0
        for _, v := range(strconv.Itoa(i)) {
            sum += int(v) - 48
        }
        if _, exists := m[sum]; exists {
            m[sum] += 1
        } else {
            m[sum] = 1
        }
    }
    lis := make([]int, 0, len(m))
    for _, v := range(m) {
        lis = append(lis, v)
    }
    
    sort.Ints(lis)
    max := lis[len(lis) - 1]
    count := 0
    for i := len(lis) - 1; i >= 0 && lis[i] == max; i-- {
        count++
    }
    
    return count
}
