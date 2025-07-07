/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    var mem = {};
    return function(...args) {
        var key = args.join(',')
        if (key in mem) {
            return mem[key];
        }
        ret = fn(...args);
        mem[key] = ret;
        return ret;
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */
