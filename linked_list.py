class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

if __name__ == "__main__":
    l = ListNode(1)
    l1= ListNode(2)
    l2 = ListNode(3)
    l3 = ListNode(4)
    l4 = ListNode(5)
    l.next = l1
    l1.next = l2

    l2.next = l3
    l3.next = l4
    l4.next = l

    curr = l4
    #ran = 2000000000 % 3
    ran = 2 % 5
    for i in range(0, ran):
        curr = curr.next
    print(curr.val)
