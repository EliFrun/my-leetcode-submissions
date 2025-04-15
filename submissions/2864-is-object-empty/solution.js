/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    try {
        return Object.keys(obj).length == 0;
    } catch (e) {
        console.log(e);
        return obj.length == 0;
    }
};
