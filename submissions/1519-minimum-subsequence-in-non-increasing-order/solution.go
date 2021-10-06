func minSubsequence(nums []int) []int {
    sort.Ints(nums)
    sum := 0
    for _, v := range(nums) {
        sum += v
    }
    
    curr_sum := 0
    start := -1
    for i, v := range(nums) {
        curr_sum += v
        sum -= v
        if curr_sum >= sum {
            start = i
            break
        }
    }
    for i, j := start, len(nums) - 1; i < j; i, j = i + 1, j - 1 {
        nums[i], nums[j] = nums[j], nums[i]
    }
    return nums[start:]
}
