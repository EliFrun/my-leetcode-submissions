/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        LinkedList<Node> tovisit = new LinkedList<Node>();
        List<List<Integer>> retList = new ArrayList<List<Integer>>();
        tovisit.add(root);
        while(!tovisit.isEmpty()){
            ArrayList<Integer> layer = new ArrayList<Integer>();
            LinkedList<Node> queue = new LinkedList<Node>();
            for(Node p: tovisit){
                try {
                    layer.add(p.val);
                    for(Node q: p.children){
                        queue.add(q);
                    }   
                } catch (Exception e){
                    
                }
            }
            if (!layer.isEmpty()){
                retList.add(layer);
            }
            tovisit = queue;
        }
        return retList;
    }
}
