/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Next *Node
 * }
 */

func connect(root *Node) *Node {
    if root == nil {
        return root
    }
    
    curr_layer := []*Node{root}
    
    for len(curr_layer) > 0 {
        next_layer := make([]*Node, 0, 0)
        for i, v := range(curr_layer) {
            if (*v).Left != nil {
                next_layer = append(next_layer, (*v).Left)
            }
            if (*v).Right != nil {
                next_layer = append(next_layer, (*v).Right)
            }
            if i < len(curr_layer) - 1 {
                (*v).Next = curr_layer[i + 1]
            }
        }
        curr_layer = next_layer
    }
	return root
}
