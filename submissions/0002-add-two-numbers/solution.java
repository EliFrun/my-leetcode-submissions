/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ret = new ListNode();
        int carry = 0;
        while (l1 != null || l2 != null) {
            int n1, n2;
            n1 = l1 != null ? l1.val : 0;
            n2 = l2 != null ? l2.val : 0;
            ListNode c = new ListNode((n1 + n2 + carry) % 10);
            carry = (n1 + n2 + carry) / 10;
            pushNode(c, ret);
            
            l1 = l1 != null ? l1.next : null;
            l2 = l2 != null ? l2.next : null;
        }
        if (carry != 0){
            pushNode(new ListNode(carry), ret);
        }
        return ret.next;
    }
    
    
    private static void pushNode(ListNode n, ListNode root){
        ListNode foo = root;
        while(foo.next != null){
            foo = foo.next;
        }
        foo.next = n;
    }
}
