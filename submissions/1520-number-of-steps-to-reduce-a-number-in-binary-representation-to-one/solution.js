/**
 * @param {string} s
 * @return {number}
 */
var numSteps = function(s) {
    if (s === "1") {
        return 0
    }
    if (s.slice(-1) === "0") {
        return 1 + numSteps(s.slice(0, -1));
    } else {
        s = binAddOne(s)
        return 1 + numSteps(s);
    }
};

var binAddOne = (s) => {
    let ret = "";
    let carry = 0;
    let i = s.length - 1;
    do {
        if (s.charAt(i) == "1") {
            ret = "0" + ret;
            carry = 1;
        } else {
            ret = "1" + ret;
            carry = 0;
        }
        i --;
    } while (i >= 0 && carry == 1);
    ret = (carry == 1 ? "1" : "") + s.slice(0, i + 1) + ret;
    return ret;
};
