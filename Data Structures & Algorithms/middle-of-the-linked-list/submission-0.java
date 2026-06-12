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
    public ListNode middleNode(ListNode head) {
        ArrayList<ListNode> arr = new ArrayList<>();
        ListNode cur = head;
        while (cur != null){
            arr.add(cur);
            cur = cur.next;
        }

        return arr.get(arr.size() / 2);
    }
}