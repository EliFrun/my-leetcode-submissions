/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return function(x) {
        var ret = x;
        functions.slice().reverse().forEach((f) => {
            ret = f(ret);
        })
        return ret;
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
