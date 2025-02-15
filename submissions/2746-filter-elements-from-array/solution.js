/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    var ret = []
    arr.forEach((e, idx) => {
        if (fn(e, idx)) {
            ret.push(e);
        }
    });
    return ret;
};
