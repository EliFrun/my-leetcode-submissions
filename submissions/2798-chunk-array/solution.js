/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    var ret = [];
    for (let i = 0; i < arr.length ; i += size) {
        ret.push(arr.slice(i, i + size));
    }
    return ret;
};

