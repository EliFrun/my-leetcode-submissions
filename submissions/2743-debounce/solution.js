/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    var time = {t: 0};
    var counter = 0;
    return function(...args) {
        time.t = counter;
        let my_val = counter;
        counter++;
        setTimeout(() => { if (time.t == my_val) { fn(...args); } }, t);
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */
