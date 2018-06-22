public class Solution
{
	public ListNode addTwoNumbers(ListNode l1, ListNode l2)
	{

		ListNode pre = new ListNode(0);
		ListNode head = pre;

		int carry = 0;

		while(l1 ! = null || l1 != null || carry != 0)
		{
			ListNode current = new ListNode(0);
			int sum = (l1 == null ? 0 : l1.val) + (l2 == null ? 0 : l2.val) + carry;
			carry = sum/10;
			int num = sum%10;
			current.val = num;
			pre.next = current;
			pre = current;

			l1 = (l1 == null ? l1 : l1.next);
			l2 = (l2 == null ? l2 : l2.next);
		}

		return head.next;
	}
}