/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
    let a = new Set();
    for (email of emails) {
        let name = email.split('@')[0].split(".").join("").split("+")[0] + '@' + email.split('@')[1];
        a.add(name);
    }
    
    return a.size;
};
