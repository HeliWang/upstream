"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5
"""

# 1->2, k = 1
# 1->2, k = 2

# Recursive Way (Better)


# 22 mins - found bug, did not connect two groups
# 29 mins - found out ways to connect two groups
"""
Bug Here:
Your input
[1,2,3,4,5]
2
Output
[5]
Expected
[2,1,4,3,5]

Last executed input
[1,2]
2
Time Limit Exceeded

Wrong Answer
Input
[1,2]
3
Output
[1]
Expected
[1,2]

"""


# Recursive way to solve the problem -- Best!
class Solution(object):
    def reverseKGroup(self, head, k):
        if not head or not head.next or k == 1: return head
        # Check if there are k nodes remaining in the current group
        end = head
        for _ in range(k - 1):
            if end is not None:
                # end will be None if current remaining length of linkedlist < k
                end = end.next
        # Find end node of the k group
        if end is None:
            return head
        head_next_group = self.reverseKGroup(end.next, k)
        end.next = None
        prev = head
        cur = head.next
        while cur:
            cur_next = cur.next
            cur.next = prev
            prev = cur
            cur = cur_next
        head.next = head_next_group
        return end


# Code with no BUG
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode

        [1,2,3,4]
        2
        """
        if not head or not head.next or k == 1: return head
        prev = head  # 2
        cur = head.next  # 3
        start = head  # 3
        end = head  # 4
        for _ in range(k - 1):
            if end is not None:
                # end will be None if current remaining length of linkedlist < k
                end = end.next
        new_head = end if end is not None else head  # 2
        if end is not None: head.next = None
        # 4<-1<-2 3<-4
        #    p c
        while cur is not None:
            # print(cur.val)
            if end is None: break
            cur_next = cur.next  # 3
            if prev != end:
                cur.next = prev  # 2.next = 1
            else:
                end = cur
                for _ in range(k - 1):
                    if end is not None:
                        # end will be None if current reaminign length of linkedlist < k
                        end = end.next
                if end is not None:
                    start.next = end
                    cur.next = None
                else:
                    start.next = cur
                start = cur
            prev = cur
            cur = cur_next
        return new_head


# Code with BUG
def reverse_k_group(head, k):
    if not head.next or k == 1: return head
    prev = head  # 1 2
    cur = head.next  # 2 None
    start = head
    end = head  # 2
    for _ in range(k - 1):
        if end is not None:
            # end will be None if current remaining length of linkedlist < k
            end = end.next
    while cur is not None:
        if end is None: break
        cur_next = cur.next
        if prev != end:
            cur.next = prev  # 2.next = 1
        else:
            end = cur
            for _ in range(k - 1):
                if end is not None:
                    # end will be None if current reaminign length of linkedlist < k
                    end = end.next
            if end is not None:
                start.next = end
            else:
                start.next = cur
            start = cur
        prev = cur
        cur = cur_next
    return prev
