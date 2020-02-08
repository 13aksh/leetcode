package com.leetcode;

import com.commons.ListNode;

public class AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode l1Head = l1;
        ListNode l2Head = l2;
        while (l1 != null || l2 != null) {
            if (l1 != null) {
                if (l2 != null) {
                    l1.val += (l2.val + carry);
                    carry = l1.val/10;
                    l1.val %= 10;
                    l2.val = l1.val;
                    if (carry != 0 && l1.next == null && l2.next == null) {
                        ListNode node = new ListNode(carry);
                        l1.next = node;
                        return l1Head;
                    }
                    l2 = l2.next;
                } else {
                    l1.val += carry;
                    carry = l1.val/10;
                    l1.val %= 10;
                    if (carry != 0 && l1.next == null) {
                        ListNode node = new ListNode(carry);
                        l1.next = node;
                        return l1Head;
                    } else if (carry == 0) {
                        return l1Head;
                    }
                }
                l1 = l1.next;
            } else {
                l2.val += carry;
                carry = l2.val/10;
                l2.val %= 10;
                if (carry != 0 && l2.next == null) {
                    ListNode node = new ListNode(carry);
                    l2.next = node;
                    return l2Head;
                }
                if (carry == 0) {
                    return l2Head;
                }
                l2 = l2.next;
            }
        }
        return l1Head;
    }
}
