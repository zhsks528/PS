/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
  if (!l1) {
    return l2;
  } else if (!l2) {
    return l1;
  }
  let reslist, head;
  if (l2.val > l1.val) {
    head = l1;
    l1 = l1.next;
  } else {
    head = l2;
    l2 = l2.next;
  }
  reslist = head;
  while (l1 && l2) {
    if (l2.val > l1.val) {
      reslist.next = l1;
      reslist = l1;
      l1 = l1.next;
    } else {
      reslist.next = l2;
      reslist = l2;
      l2 = l2.next;
    }
  }

  if (l1) {
    reslist.next = l1;
  } else {
    reslist.next = l2;
  }
  return head;
};
