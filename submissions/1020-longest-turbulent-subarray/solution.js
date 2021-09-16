/**
 * @param {number[]} arr
 * @return {number}
 */
var maxTurbulenceSize = function(arr) {
    a = []
    for (let i = 1; i < arr.length; i++) {
        let b = 0;
        if (arr[i] > arr[i - 1]) {
            b = 1;
        } else if (arr[i] < arr[i - 1]) {
            b = -1;
        } else {
            b = 0;
        }
        a.push(b);
    }
    if (a.length == 0) {
        return 1;
    }
    if (a.length == 1) {
        return a[0] == 0 ? 1 : 2;
    }
    let [index, curr, max] = [0, (a[0] == 0 ? 0 : 1), 0];
    while (index < a.length - 1) {
        if (a[index + 1] != 0 && a[index] != a[index + 1]) {
            curr += 1;
        } else {
            max = Math.max(curr, max);
            curr = a[index + 1] == 0 ? 0 : 1;
        }
        index++;
    }
    return Math.max(curr, max) + 1;   
};
