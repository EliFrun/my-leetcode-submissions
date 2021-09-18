/**
 * @param {number[]} nums
 * @return {number}
 */
var tupleSameProduct = function(nums) {
    let lis = {};
    
    for (let i = 0; i < nums.length - 1; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            let [a, b] = [nums[i], nums[j]];
            if (a * b in lis){
                lis[a * b] += 1;
            } else {
                lis[a * b] = 1;
            }
        }
    }
    let ret = 0;
    const factorial = (n) => {
        if (n <= 1) {
            return 1
        }
        return n * factorial(n - 1);
        
    };
    for (let [_, v] of Object.entries(lis)){
        if (v < 2){
            continue;
        } else {
            ret += 8 * factorial(v)/(2 * factorial(v - 2));
        }
    }
    
    return ret;
};
