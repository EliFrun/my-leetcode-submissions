/**
 * // Definition for a Node.
 * function Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {Node|null} root
 * @return {number[]}
 */
var postorder = function(root) {
    if (root == null) {
        return []
    } else {
        let ret = [];
        root.children.forEach((v) => {
           ret = [...ret, ...postorder(v)] 
        });
        return [...ret, root.val]
    }
    
};
