/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    if (arr.length <= 1) {
        return arr;
    }

    if (arr.length == 2) {
        return fn(arr[0]) < fn(arr[1]) ? arr : arr.reverse();
    }

    let left = sortBy(arr.slice(0, Math.round(arr.length / 2)), fn);
    let right = sortBy(arr.slice(Math.round(arr.length / 2)), fn);
    let i = j = 0;
    let ret = [];
    while (i < left.length && j < right.length) {
        if (fn(left[i]) < fn(right[j])) {
            ret.push(left[i]);
            i++;
        } else {
            ret.push(right[j]);
            j++;
        }
    }    
    while (i < left.length) {
        ret.push(left[i]);
        i++;
    }
    while (j < right.length) {
        ret.push(right[j]);
        j++;
    }
    return ret;
};
